import tweepy
import os
from nltk import tokenize
from config import create_api
import news_ops
import logging
import time
import json
import random
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

according_to = ["NYT ", "CBS ", "FOX ", "MSNBC ", "CNN ", "WSJ ", "DOW "]

random.seed(time.time())

SECONDS = 15


def get_article(fil):
    """
    returns a list of all the available articles to extract
    """
    random.seed(time.time())

    a_file = open(fil, "r")

    list_of_lists = []
    for line in a_file:
        list_of_lists.append(line.strip())

    a_file.close()
    return list_of_lists


def random_date():
    """
    gets a random date to associate with the article
    """
    random.seed(time.time())
    d = random.randint(1, int(time.time()))
    return f'({str(datetime.date.fromtimestamp(d).strftime("%Y-%m-%d"))}): '


def get_random_str(main_str):
    """
    gets a random sentence from the article with the help of nltk
    """
    random.seed(time.time())
    sentences = tokenize.sent_tokenize(main_str)
    random_sentence = random.choice(sentences)

    # asserts that line can fit in tweet
    while len(random_sentence) < 30 or len(random_sentence) > 200:
        random_sentence = random.choice(sentences)

    # quotes end with quotes
    if random_sentence.startswith('“'):
        random_sentence += '”'
    return random.choice(according_to) + random_date() + random_sentence


def content_list(lst):
    """
    returns a list of sentences we want to tweet
    """
    news_content = []

    for ex in lst:
        body = news_ops.get_the_onion_article(ex)
        news = get_random_str(body)
        news_content.append(news)

    return news_content


def tweet(api):
    """
    tweets the articles every few seconds
    """
    logger.info("Tweeting content")
    urls = get_article('the_onion.txt')
    lines = content_list(urls)

    for line in lines:
        try:
            api.update_status(line)
            logger.info("Tweeting!")
            time.sleep(SECONDS)

        except tweepy.TweepError as err:
            logger.error(err)


def main():
    logger.info("Program start")
    api = create_api()
    while True:
        tweet(api)
    logger.info("Program complete")


if __name__ == "__main__":
    main()
