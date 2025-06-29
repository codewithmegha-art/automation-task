📦 S3 Archive to Glacier Using AWS Lambda and Boto3
 

 ✅ Objective
Automate the archival of S3 objects older than 6 months to Amazon Glacier storage class for cost savings. 

✅ 1️⃣ S3 Setup
Created a new S3 bucket in the AWS console.

Uploaded a mix of older and newer files for testing. 

✅ 2️⃣ IAM Role Setup
Created a new IAM Role for Lambda.

Attached the AmazonS3FullAccess policy. 


✅ 3️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

Assigned IAM Role: The role created above

Configured timeout and memory as needed. 

✅ 4️⃣ Lambda Function Code
Uses Boto3 to:

List objects in the S3 bucket

Check if they are older than 6 months

Change their storage class to GLACIER if needed

Log the archived objects 

✅ Files Included
lambda_function.py – The Lambda function code

images/ – Screenshots of all steps

step.md – This documentation