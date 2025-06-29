🔐 Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3 

✅ Objective
Automate detection of any S3 buckets without server-side encryption using AWS Lambda and Boto3. 

✅ 1️⃣ S3 Setup
Created multiple S3 buckets.

Ensured some of them do not have server-side encryption enabled. 

 2️⃣ IAM Role Setup
Created a new IAM role for Lambda.

Attached the AmazonS3ReadOnlyAccess policy.

This allows listing buckets and reading their encryption configuration. 


✅ 3️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

IAM Role: The role created above

Configured basic settings (timeout, memory, environment) 


✅ 4️⃣ Lambda Function Code
Used Boto3 to:

List all S3 buckets

Attempt to get each bucket’s encryption configuration

Identify buckets without server-side encryption

Print unencrypted buckets in logs 


✅ 5️⃣ Manual Invocation and Testing
Manually invoked the Lambda function from AWS Console.

Checked logs in CloudWatch for output:

Listed unencrypted buckets successfully. 


✅ Conclusion
✅ Successfully detected S3 buckets without server-side encryption.
✅ Verified output in Lambda logs.
✅ Demonstrated AWS security posture monitoring using Boto3 and Lambda. 

✅ Files Included
lambda_function.py – The Lambda code

images/ – Screenshots

step.md – This documentation