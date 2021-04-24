import tweepy
import os
import logging
from dotenv import load_dotenv
import time
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

load_dotenv()

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET')

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = os.getenv('BEARER_TOKEN')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline).items():
    # process status here
    print(status)