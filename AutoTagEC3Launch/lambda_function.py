import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get the instance ID from the event
    instance_id = event['detail']['instance-id']

    # Get current date
    today = datetime.now().strftime('%Y-%m-%d')

    # Tag EC2 instance
    response = ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {'Key': 'LaunchDate', 'Value': today},
            {'Key': 'CreatedBy', 'Value': 'AutoTag-Lambda'}
        ]
    )

    print(f"✅ Tagged instance {instance_id} with LaunchDate={today} and CreatedBy=AutoTag-Lambda")
