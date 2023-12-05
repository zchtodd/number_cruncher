FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

RUN apk update && apk add --no-cache postgresql-dev && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /usr/src/app
