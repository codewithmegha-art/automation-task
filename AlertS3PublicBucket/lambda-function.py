import boto3
import botocore
import os
import json

# Create AWS service clients
sns_client = boto3.client('sns')
s3_client = boto3.client('s3')

# Get SNS Topic ARN from environment variable
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def is_acl_public(acl):
    """
    Checks if the bucket's ACL grants access to AllUsers (public).
    """
    for grant in acl.get('Grants', []):
        grantee = grant.get('Grantee', {})
        if grantee.get('Type') == 'Group' and 'AllUsers' in grantee.get('URI', ''):
            return True
    return False

def is_policy_public(policy_json):
    """
    Checks if the bucket policy allows access to "*" (everyone).
    """
    policy = json.loads(policy_json)
    for statement in policy.get('Statement', []):
        principal = statement.get('Principal')
        effect = statement.get('Effect')
        
        if effect == 'Allow':
            if principal == "*":
                return True
            if isinstance(principal, dict):
                aws_principal = principal.get('AWS')
                if aws_principal == "*" or aws_principal == ["*"]:
                    return True
    return False

def lambda_handler(event, context):
    public_buckets = []

    try:
        response = s3_client.list_buckets()
        buckets = response['Buckets']
    except Exception as e:
        print(f"Error listing buckets: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to list S3 buckets')
        }

    for bucket in buckets:
        bucket_name = bucket['Name']
        print(f"Checking bucket: {bucket_name}")
        is_public = False

        # Check ACL
        try:
            acl = s3_client.get_bucket_acl(Bucket=bucket_name)
            if is_acl_public(acl):
                print(f"Bucket {bucket_name} has a public ACL!")
                is_public = True
        except Exception as e:
            print(f"Error getting ACL for {bucket_name}: {e}")

        # Check Policy
        try:
            policy_response = s3_client.get_bucket_policy(Bucket=bucket_name)
            if is_policy_public(policy_response['Policy']):
                print(f"Bucket {bucket_name} has a public Policy!")
                is_public = True
        except botocore.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'NoSuchBucketPolicy':
                # This bucket has no policy attached
                print(f"Bucket {bucket_name} has no bucket policy.")
            else:
                print(f"Error getting policy for {bucket_name}: {e}")
        except Exception as e:
            print(f"Unexpected error getting policy for {bucket_name}: {e}")

        if is_public:
            public_buckets.append(bucket_name)

    if public_buckets:
        # Prepare the alert message
        message = "⚠️ Public S3 Buckets Detected:\n\n" + "\n".join(public_buckets)
        print("Sending SNS notification...")
        
        try:
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="ALERT: Public S3 Buckets Found",
                Message=message
            )
            print("Notification sent!")
        except Exception as e:
            print(f"Error sending SNS notification: {e}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Public buckets found and notification sent: {public_buckets}')
        }
    else:
        print("✅ No public buckets found.")
        return {
            'statusCode': 200,
            'body': json.dumps('No public buckets found.')
        }
