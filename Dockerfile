FROM python:3.9.1
LABEL maintainer="Chiah Soon <chiahsoon18@gmail.com>"
COPY ./ ./app
WORKDIR ./app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# docker build -t chiahsoon/flask-scaffold:0.0.1 .