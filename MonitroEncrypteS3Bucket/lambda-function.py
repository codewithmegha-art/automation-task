import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
            rules = encryption['ServerSideEncryptionConfiguration']['Rules']
            # If rules exist, encryption is enabled
        except s3.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                unencrypted_buckets.append(bucket_name)
            else:
                print(f"Error checking bucket {bucket_name}: {str(e)}")

    if unencrypted_buckets:
        print("Unencrypted S3 Buckets found:")
        for name in unencrypted_buckets:
            print(f" - {name}")
    else:
        print("All buckets have server-side encryption enabled.")
