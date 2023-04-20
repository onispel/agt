# FROM  python:latest
from alpine:latest

RUN apk add --no-cache python3 py3-pip

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .
COPY pyproject.toml .
COPY . .

COPY .aws /root/.aws

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e .
