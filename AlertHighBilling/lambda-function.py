import boto3
from datetime import datetime, timedelta

# === CONFIGURATION ===
THRESHOLD = 50.0  # USD
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:892513402687:BillingAlertTopic'

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')

    # Get estimated billing
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[
            {'Name': 'Currency', 'Value': 'USD'}
        ],
        StartTime=datetime.utcnow() - timedelta(days=1),
        EndTime=datetime.utcnow(),
        Period=86400,
        Statistics=['Maximum']
    )

    datapoints = response['Datapoints']
    if not datapoints:
        print("⚠️ No billing data available.")
        return

    latest_datapoint = max(datapoints, key=lambda x: x['Timestamp'])
    amount = latest_datapoint['Maximum']
    print(f"📊 Current AWS bill: ${amount:.2f}")

    if amount > THRESHOLD:
        message = f"🔔 ALERT: Your AWS bill is ${amount:.2f}, which exceeds your threshold of ${THRESHOLD:.2f}."
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='AWS Billing Alert',
            Message=message
        )
        print("✅ Alert sent to SNS topic.")
    else:
        print("✅ Billing is under control.")


