import boto3
from datetime import datetime, timezone, timedelta
import logging

# Logging setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create S3 client
s3 = boto3.client('s3')

# Config
BUCKET_NAME = 'my-archive-file-bucket'  # Replace with your actual bucket name
GLACIER_CLASS = 'GLACIER'         # or 'DEEP_ARCHIVE' for deeper storage
DAYS_OLD_THRESHOLD = 1         # 1 days = days

def lambda_handler(event, context):
    # Get current date
    now = datetime.now(timezone.utc)

    # List all objects in the S3 bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    if 'Contents' not in response:
        logger.info("Bucket is empty.")
        return

    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']
        
        # Calculate object age
        age = (now - last_modified).days

        if age >= DAYS_OLD_THRESHOLD and obj['StorageClass'] == 'STANDARD':
            logger.info(f"Archiving file: {key}, Age: {age} days")
            
            # Copy the object to same location with new storage class
            s3.copy_object(
                Bucket=BUCKET_NAME,
                Key=key,
                CopySource={'Bucket': BUCKET_NAME, 'Key': key},
                StorageClass=GLACIER_CLASS,
                MetadataDirective='COPY'
            )

            # Optionally, you can delete the old version after copy (but not required)
        else:
            logger.info(f"Skipping file: {key}, Age: {age} days")
