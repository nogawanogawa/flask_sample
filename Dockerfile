FROM ubuntu:18.04

# Pythonのインストール
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip

# ライブラリのインストール
RUN pip3 install flask
RUN pip3 install --upgrade flask
RUN pip3 install flask-cors
RUN pip3 install elasticsearch
RUN pip3 install pytest

# 環境変数の調整
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV APP_PATH=/home
WORKDIR $APP_PATH
ENV HOME $APP_PATH
ENV PYTHONPATH $APP_PATH
ENV FLASK_APP microservice

CMD [ "/bin/sh" ]