import tweepy
import logging
from dotenv import load_dotenv
import os 
import creds

logger = logging.getLogger()

def create_api():
    consumer_key = creds.API_KEY
    consumer_secret = creds.API_SECRET

    access_token = creds.ACCESS_TOKEN
    access_token_secret = creds.ACCESS_TOKEN_SECRET

    auth = creds.BEARER_TOKEN

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
        
    logger.info("API created")
    return api