📝 Sentiment Analysis of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend 

✅ Objective
Automatically analyze and categorize the sentiment of user reviews using Amazon Comprehend.
Process reviews via AWS Lambda and log results for downstream use. 

✅ 1️⃣ IAM Role Setup
Created a new IAM Role for Lambda in AWS Console.

Attached the policy:

AmazonComprehendFullAccess (or custom minimum permissions) 


✅ 2️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

Assigned IAM Role: The role created above

Configured timeout and memory settings as needed. 

✅ 3️⃣ Lambda Function Code
Uses Boto3 to:

Extract review text from the event

Call Amazon Comprehend to detect sentiment

Log the sentiment and score 


✅ 4️⃣ Testing
Manually invoked the Lambda function with sample payload:

json
Copy
Edit
{
  "review": "I love this product! It's amazing and works perfectly."
} 

Verified CloudWatch logs showing:

Sentiment: POSITIVE

SentimentScore with confidence scores 


✅ Files Included
lambda_function.py – The Lambda function code

images/ – Screenshots of all steps

step.md – This documentation