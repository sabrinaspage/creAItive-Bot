import requests
import logging as LOG
from bs4 import BeautifulSoup

def get_news(url):
    try:
        news_article = requests.get(url)
        news_article.raise_for_status()

        LOG.info('Obtained Issues for URL {}: {}'.format(url, news_article))
        return news_article

    except requests.exceptions.HTTPError as e:
        LOG.error("Error for project {}:\n{}".format(e))
        raise e

def get_the_onion_article(url):
    news = get_news(url)
    soup = BeautifulSoup(news.text, "html.parser")
    full_text = []
    diff_bodies = soup.find_all("p", {"class": "sc-77igqf-0 bOfvBY"})
    for body in diff_bodies:
        full_text.append(body.getText())

    return ' '.join(full_text)