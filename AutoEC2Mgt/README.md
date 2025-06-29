Automated EC2 Instance Management Using AWS Lambda and Boto3 

📌 Description
This project automates the starting and stopping of EC2 instances based on their tags using AWS Lambda and Boto3.

✅ Objective
Stop EC2 instances with tag Action=Auto-Stop

Start EC2 instances with tag Action=Auto-Start 

✅ Steps Followed 

1️⃣ EC2 Setup
Created two t2.micro instances.

Added the following tags:

Instance 1: Action = Auto-Stop

Instance 2: Action = Auto-Start 

2️⃣ IAM Role Setup
Created a new IAM Role for Lambda.

Attached the policy AmazonEC2FullAccess. 

3️⃣ Lambda Function Creation
Created a new Lambda function in AWS Console.

Runtime: Python 3.x

Assigned the IAM Role. 

4️⃣ Lambda Function Code
Used Boto3 to describe instances, stop Auto-Stop instances, and start Auto-Start instances.

✅ Code is in lambda_function.py 

5️⃣ Manual Invocation and Testing
Manually triggered the Lambda function.

Verified instance state changes in AWS Console. 

✅ Conclusion
Successfully implemented automation using AWS Lambda and Boto3 to manage EC2 instances based on tags. 

✅ Files Included
lambda_function.py : Lambda code

images/ : Screenshots

README.md : Documentation