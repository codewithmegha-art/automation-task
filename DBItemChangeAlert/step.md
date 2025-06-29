⚡️ DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS

✅ Objective
Automate alerts when items in a DynamoDB table are updated.
Use AWS Lambda to process DynamoDB Streams and send email notifications via SNS. 

✅ 1️⃣ DynamoDB Setup
Created a DynamoDB table in AWS Console.

Added several sample items for testing. 


✅ 2️⃣ SNS Setup
Created an SNS Topic in AWS Console.

Subscribed email address for notifications.

Confirmed the subscription. 

✅ 3️⃣ IAM Role Setup
Created a new IAM Role for Lambda.

Attached these policies:

AmazonDynamoDBReadOnlyAccess

AmazonSNSFullAccess

AWSLambdaDynamoDBExecutionRole 

✅ 4️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

IAM Role: The role created above

Configured basic settings like timeout and memory. 

✅ 5️⃣ Lambda Function Code
Uses Boto3 to:

Process records from DynamoDB Stream events

Extract old and new images for updates

Format and send an SNS alert with the change details 

✅ 6️⃣ DynamoDB Stream Setup
Enabled DynamoDB Streams on the table.

View type: New and old images

Configured the stream to trigger the Lambda function automatically. 

✅ Files Included
lambda_function.py – The Lambda function code

images/ – Screenshots of setup and results

step.md – This documentation

