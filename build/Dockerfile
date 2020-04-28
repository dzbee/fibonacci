FROM python:3.7-buster

COPY . /app
WORKDIR /app

RUN pip install -r build/requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]