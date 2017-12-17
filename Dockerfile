FROM python:3
MAINTAINER Hypercube <hypercube@0x01.me>
EXPOSE 80

WORKDIR /cpa

RUN pip install --no-cache-dir django
COPY . .
ENV DEBUG=false

CMD python3 manage.py runserver 0:80
