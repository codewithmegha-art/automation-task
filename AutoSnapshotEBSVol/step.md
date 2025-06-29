💾 Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3 

✅ Objective
Automate the creation of EBS snapshots for backup and clean up snapshots older than 30 days using AWS Lambda and Boto3.

✅ 1️⃣ EBS Setup
Identified/created an EBS volume to back up.

Noted down the Volume ID for use in the Lambda function. 



✅ 2️⃣ IAM Role Setup
Created a new IAM role for Lambda.

Attached the AmazonEC2FullAccess policy to allow:

Creating snapshots

Deleting snapshots

Describing snapshots 


✅ 3️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

IAM Role: The role created above

Configured timeout and memory settings. 


✅ 4️⃣ Lambda Function Code
Used Boto3 to:

Create a snapshot for the specified EBS volume

List snapshots for that volume

Delete snapshots older than 30 days

Log the IDs of created and deleted snapshots 


✅ 5️⃣ Manual Invocation and Testing
Manually invoked the Lambda function in AWS Console.

Reviewed logs showing:

Snapshot creation

Old snapshots deleted 


✅ Files Included
lambda_function.py – The Lambda function code

images/ – Screenshots for documentation

step.md – This documentation