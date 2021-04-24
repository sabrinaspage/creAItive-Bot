FROM python:3.7-alpine

COPY twitter_bot.py /
CMD ["python3", "twitter_bot.py"]