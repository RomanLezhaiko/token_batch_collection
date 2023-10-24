FROM python:3.11.6-alpine3.18

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV AMOUNT_ON_BALANCE 0.01

RUN apk update && apk add bash 

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt