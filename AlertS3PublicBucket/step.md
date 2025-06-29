🛡️ S3 Bucket Public Access Audit Using AWS Lambda, Boto3, and SNS 


✅ Objective
Automatically audit S3 bucket permissions and notify if any buckets have public read or write permissions.

✅ 1️⃣ SNS Setup
Created a new SNS topic in AWS Console.

Subscribed email for receiving alerts.

Confirmed the subscription.

✅ 2️⃣ IAM Role Setup
Created a new IAM Role for Lambda.

Attached these permissions:

AmazonS3ReadOnlyAccess

AmazonSNSFullAccess 


✅ 3️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

Assigned IAM Role: The role created above

Configured timeout and memory as needed. 


✅ 4️⃣ Lambda Function Code
Uses Boto3 to:

List all S3 buckets.

Check ACLs and bucket policies for public access.

If public → sends alert via SNS. 


✅ 5️⃣ CloudWatch Events Schedule
Created a CloudWatch Events rule to trigger Lambda daily.

Automates the audit without manual intervention. 



✅ 6️⃣ Testing
Made one or two S3 buckets public.

Ran the Lambda function manually.

Verified:

S3 bucket permission settings:

✅ Screenshot:

CloudWatch logs of Lambda execution:

✅ Screenshot:

Received SNS email alert: 


 Files Included
lambda_function.py – Lambda function code

images/ – Screenshots of all steps

step.md – This documentation