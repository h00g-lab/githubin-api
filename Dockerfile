FROM python:3.6-slim-buster

WORKDIR app

COPY * /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 80

# CMD ["flask", "run", "--port=80"]
