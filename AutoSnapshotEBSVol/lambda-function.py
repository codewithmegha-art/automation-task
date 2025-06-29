import boto3
from datetime import datetime, timezone, timedelta

# Replace with your volume ID
VOLUME_ID = 'vol-03b6d60450aaf024a'
RETENTION_MINUTES = 1  # ⏱ Keep snapshots only for 1 minute

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
   
    # ✅ Step 2: Cleanup Old Snapshots
    snapshots = ec2.describe_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [VOLUME_ID]},
            {'Name': 'description', 'Values': [f"Backup for {VOLUME_ID}*"]}
        ],
        OwnerIds=['self']
    )

    for snap in snapshots['Snapshots']:
        start_time = snap['StartTime']
        snapshot_id = snap['SnapshotId']
        
        # 🧹 Delete if older than 1 minute
        if start_time.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc) - timedelta(minutes=RETENTION_MINUTES):
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"🗑️ Deleted old snapshot: {snapshot_id}")
