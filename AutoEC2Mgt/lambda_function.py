import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Fetch all instances
    response = ec2.describe_instances()

    # Lists to store instance IDs
    auto_stop_instances = []
    auto_start_instances = []

    # Loop through instances and check tags
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            tags = instance.get('Tags', [])
            for tag in tags:
                if tag['Key'] == 'Action' and tag['Value'] == 'Auto-Stop':
                    auto_stop_instances.append(instance_id)
                elif tag['Key'] == 'Action' and tag['Value'] == 'Auto-Start':
                    auto_start_instances.append(instance_id)

    # Stop instances
    if auto_stop_instances:
        print(f"Stopping instances: {auto_stop_instances}")
        ec2.stop_instances(InstanceIds=auto_stop_instances)

    # Start instances
    if auto_start_instances:
        print(f"Starting instances: {auto_start_instances}")
        ec2.start_instances(InstanceIds=auto_start_instances)

    return {
        'statusCode': 200,
        'body': f"Stopped: {auto_stop_instances}, Started: {auto_start_instances}"
    }
