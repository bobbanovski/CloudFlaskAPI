#
#
# Pets-API Dockerfile
#

#Pull base image
FROM python:3.4.5-slim

#Get custom packages
RUN apt-get update && apt-get install -y \
    build-essential \
    make \
    gcc \
    python3-dev \
    mongodb

##make a local directory
RUN mkdir /opt/cloudFlask-api

WORKDIR /opt/cloudFlask-api

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python manage.py runserver