FROM python:3.8.2-alpine
MAINTAINER ORKA Solutions

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --update --no-cache \
      mariadb-client gcc libc-dev linux-headers mariadb-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /code/entrypoint.sh

# copy lmsapi
COPY . /code/

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
