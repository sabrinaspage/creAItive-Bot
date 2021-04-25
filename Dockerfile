FROM python:3.7-alpine

COPY config.py /
COPY creAItive_bot.py /
COPY requirements.txt /
COPY creds.py /
COPY news_ops.py /
COPY the_onion.txt /
COPY README.md /

RUN pip install -U pip
RUN pip install -U setuptools
RUN pip3 install nltk
RUN pip install -r requirements.txt

CMD ["python3", "creAItive_bot.py"]