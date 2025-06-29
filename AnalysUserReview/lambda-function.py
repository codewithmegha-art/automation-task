import boto3
import json
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Comprehend client
comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    try:
        # 1. Extract the review text from the event
        review = event.get('review', '')
        
        if not review:
            logger.error("No review provided in the event.")
            return {
                'statusCode': 400,
                'body': json.dumps('Missing review text')
            }
        
        # 2. Call Amazon Comprehend to analyze sentiment
        response = comprehend.detect_sentiment(
            Text=review,
            LanguageCode='en'  # 'en' = English
        )

        # 3. Extract the sentiment
        sentiment = response['Sentiment']
        sentiment_score = response['SentimentScore']

        # 4. Log and return the result
        logger.info(f"Review: {review}")
        logger.info(f"Sentiment: {sentiment}")
        logger.info(f"SentimentScore: {sentiment_score}")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'Sentiment': sentiment,
                'Scores': sentiment_score
            })
        }

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }
