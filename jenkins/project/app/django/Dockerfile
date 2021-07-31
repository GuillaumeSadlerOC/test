# pull official base image
FROM python:3.8

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set work directory
RUN mkdir -p /usr/src/projects

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /usr/src/projects/app_1
WORKDIR /usr/src/projects/app_1

# install dependencies
RUN apt-get update && apt-get install -y gettext
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
