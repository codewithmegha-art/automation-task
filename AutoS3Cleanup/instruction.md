
🗑️ Automated S3 Bucket Cleanup Using AWS Lambda and Boto3 

✅ Objective
Automate deletion of files older than 30 days in an S3 bucket using AWS Lambda and Boto3. 

✅ 1️⃣ S3 Setup
Created a new S3 bucket.
Uploaded multiple files, some older than 30 days (using old file timestamps or metadata). 


✅ 2️⃣ IAM Role Setup
Created a new IAM Role for Lambda.

Attached the AmazonS3FullAccess policy to allow:
Listing objects
Deleting objects 



✅ 3️⃣ Lambda Function Creation
Created a new AWS Lambda function:

Runtime: Python 3.x
Assigned the IAM Role created above
Set basic config (timeout, memory) 

✅ 4️⃣ Lambda Function Code
Used Boto3 to:

List all objects in the bucket

Check LastModified date

Delete objects older than 30 days

Log deleted files 


✅ 5️⃣ Manual Invocation and Testing
Manually invoked the Lambda function in AWS Console.

Checked logs to confirm which files were deleted. 


✅ Conclusion
✅ Successfully automated cleanup of old files in S3 using AWS Lambda and Boto3.
✅ Verified removal of objects older than 30 days.
✅ Confirmed correct IAM role and permissions. 


✅ Files Included
lambda_function.py – Lambda code

images/ – Screenshots for documentation

README.md – This documentation