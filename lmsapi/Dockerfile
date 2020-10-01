FROM python:3.8.5-alpine
MAINTAINER ORKA Solutions
ENV APP_HOME /usr/src/app

RUN mkdir -p $APP_HOME
# set work directory
WORKDIR $APP_HOME
RUN mkdir static
RUN mkdir media
RUN mkdir gstatic

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --update --no-cache \
      mariadb-client gcc libc-dev linux-headers mariadb-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh ./entrypoint.sh

# copy lmsapi
COPY ./ ./

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
