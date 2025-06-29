💰 AWS Billing Alert Using Lambda, Boto3, and SNS 

 ✅ Objective
Automate AWS billing monitoring.
Alert via SNS email when billing exceeds a defined threshold (e.g., $50). 


✅ 1️⃣ SNS Setup
Created a new SNS Topic in AWS Console.

Subscribed my email address to this topic.

Verified email subscription. 


✅ 2️⃣ IAM Role Setup
Created a new IAM role for Lambda.

Attached these policies:

CloudWatchReadOnlyAccess

AmazonSNSFullAccess 


✅ 3️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

IAM Role: The role created above

Configured timeout, memory as needed. 


✅ 4️⃣ Lambda Function Code
Initializes boto3 clients for:

CloudWatch – to get billing metrics

SNS – to send alerts

Retrieves the latest estimated AWS charges from CloudWatch.

Compares against a $50 threshold.

If billing exceeds threshold, sends an SNS email notification. 


✅ 5️⃣ Manual Invocation and Testing
Manually invoked the Lambda function.

Checked logs in CloudWatch for:

Retrieved billing data

Compared to threshold

SNS notification sent if over threshold 


✅ Files Included
lambda_function.py – The Lambda function code

images/ – Screenshots

step.md – This documentation     