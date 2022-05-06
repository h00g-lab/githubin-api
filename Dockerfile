FROM python:3.6-slim-buster

WORKDIR app

COPY * /app/

RUN pip install -r requirements.txt

EXPOSE 80