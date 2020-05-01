FROM python:3.7-buster

COPY . /app
WORKDIR /app

RUN pip install -r build/requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT wsgi