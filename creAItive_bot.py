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

according_to_1 = "NY7 "
according_to_2 = "CB$ "
according_to_3 = "F0X "
according_to_4 = "M$NBC "
according_to_5 = "CMM "

according_to = [according_to_1, according_to_2,
                according_to_3, according_to_4, according_to_5]

random.seed(time.time())


def get_article(fil):
    a_file = open(fil, "r")

    list_of_lists = []
    for line in a_file:
        list_of_lists.append(line.strip())

    a_file.close()
    return list_of_lists


def random_date():
    random.seed(time.time())
    d = random.randint(1, int(time.time()))
    return f'({str(datetime.date.fromtimestamp(d).strftime("%Y-%m-%d"))}): '


def get_random_str(main_str):
    random.seed(time.time())
    sentences = tokenize.sent_tokenize(main_str)
    random_sentence = random.choice(sentences)
    while len(random_sentence) < 30 or len(random_sentence) > 200:
        random_sentence = random.choice(sentences)
    if random_sentence.startswith('“'):
        random_sentence += '”'
    return random.choice(according_to) + random_date() + random_sentence


def content_list(lst):
    news_content = []

    for ex in lst:
        body = news_ops.get_the_onion_article(ex)
        news = get_random_str(body)
        news_content.append(news)

    return news_content


def tweet(api):
    logger.info("Tweeting content")
    urls = get_article('the_onion.txt')
    lines = content_list(urls)

    for line in lines:
        try:
            api.update_status(line)
            logger.info("Tweeting!")
            time.sleep(30)

        except tweepy.TweepError as err:
            logger.error(err)


def main():
    logger.info("Program start")
    api = create_api()
    tweet(api)
    logger.info("Program complete")


if __name__ == "__main__":
    main()
