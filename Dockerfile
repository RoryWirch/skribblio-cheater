FROM python:3.7.3

WORKDIR /usr/src/app

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install -e .