import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client('sns')
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:892513402687:DynamoDBItemUpdateAlert'

def lambda_handler(event, context):
    if 'Records' not in event:
        logger.warning("No 'Records' key in the event")
        return {"status": "no records"}
        
    for record in event['Records']:
        if record['eventName'] == 'MODIFY':
            old_image = record['dynamodb']['OldImage']
            new_image = record['dynamodb']['NewImage']
            
            message = {
                'Old Item': old_image,
                'New Item': new_image
            }

            logger.info(f"Detected update: {json.dumps(message)}")

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject='DynamoDB Item Updated',
                Message=json.dumps(message, default=str)
            )
    return {"status": "done"}
