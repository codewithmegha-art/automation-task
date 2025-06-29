🚨 ELB 5xx Error Spike Notification Using AWS Lambda, Boto3, and SNS 

 
 ✅ Objective
Automatically monitor 5xx error spikes on an Application Load Balancer (ALB) and send alerts using SNS. 

✅ 1️⃣ SNS Setup
Created an SNS topic in AWS Console.

Subscribed email for receiving alerts.

Confirmed the subscription. 


✅ 2️⃣ IAM Role Setup
Created a new IAM Role for Lambda.

Attached these policies:

CloudWatchReadOnlyAccess

AmazonSNSFullAccess 


✅ 3️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x

Assigned IAM Role: The role created above

Configured timeout and memory as needed. 


✅ 5️⃣ CloudWatch Events Schedule
Created a CloudWatch Events rule:

Schedule: Every 5 minutes

Target: Lambda function

This automates the check.  


✅ 6️⃣ Testing
Simulated/spotted high 5xx error spike on ALB.

Verified CloudWatch metric:

✅ Screenshot:

Lambda CloudWatch logs showed invocation and metrics:

✅ Screenshot:

Received SNS email alert:


✅ 7️⃣ Conclusion
✅ Automated 5xx error monitoring for ALB.
✅ Alerts sent via SNS if error count exceeds threshold.
✅ Fully serverless and cost-effective.