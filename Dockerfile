FROM python:3.11.9-alpine3.20

COPY requirements.txt /temp/requirements.txt
COPY sushiapp /sushiapp
WORKDIR /sushiapp
EXPOSE 8000

# RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password sushishop-user

USER sushishop-user
