FROM ubuntu:16.04

RUN apt-get update && apt-get install -y build-essential python-dev python-pip libgeos-dev python-dev swig libssl-dev libffi-dev libncurses5-dev \
                                         libjpeg-dev libfreetype6-dev zlib1g-dev libpq-dev libmysqlclient-dev inotify-tools tzdata wget libbz2-dev \
                                         libsqlite3-dev locales

RUN cd /
RUN wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
RUN tar -xvf Python-3.6.9.tgz
WORKDIR /Python-3.6.9

RUN ./configure --enable-ipv6
RUN make
RUN make install

WORKDIR /server
COPY foodhub/test_requirements.txt /server/
COPY foodhub/requirements.txt /server/
RUN pip3 install -r ./test_requirements.txt
COPY . /server/



