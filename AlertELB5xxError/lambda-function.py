import boto3
from datetime import datetime, timedelta

# === CONFIGURATION ===
ELB_NAME = 'arn:aws:elasticloadbalancing:ap-south-1:892513402687:loadbalancer/app/load-balancer-elb/25a82a75279375c5'  # Replace with your ELB name
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:892513402687:ELB-5xx-Alert'
ERROR_THRESHOLD = 0

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')

    # Time range: last 5 minutes
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=5)

    # Get 5xx errors from ELB
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/ApplicationELB',
        MetricName='HTTPCode_ELB_5XX_Count',
        Dimensions=[
            {'Name': 'LoadBalancer', 'Value': ELB_NAME}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,  # 5 minutes in seconds
        Statistics=['Sum']
    )

    datapoints = response.get('Datapoints', [])
    error_count = datapoints[0]['Sum'] if datapoints else 0

    print(f"ELB 5xx errors in last 5 minutes: {error_count}")

    if error_count >=  ERROR_THRESHOLD:
        message = f"ALERT: ELB {ELB_NAME} had {error_count} 5xx errors in last 5 minutes."
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=message, Subject='ELB 5xx Error Alert')
