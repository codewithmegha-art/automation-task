import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    BUCKET_NAME = 'my-s3-bucket-cleanup'
    s3 = boto3.client('s3')

    now = datetime.now(timezone.utc)
    threshold_date = now - timedelta(days = 30)  # Corrected: timezone-aware

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    deleted_files = []

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            last_modified = obj['LastModified']

            if last_modified < threshold_date:
                print(f"Deleting {key} (Last modified: {last_modified})")
                s3.delete_object(Bucket=BUCKET_NAME, Key=key)
                deleted_files.append(key)
            else:
                print(f"Keeping {key} (Last modified: {last_modified})")
    else:
        print("No files found in the bucket.")
    
    return {
        'statusCode': 200,
        'body': f"Deleted files: {deleted_files}"
    }
