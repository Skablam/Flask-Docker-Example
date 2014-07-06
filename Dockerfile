FROM ubuntu:12.04
MAINTAINER Skablam
RUN apt-get -qq update
RUN apt-get -qqy install python python-pip
ADD requirements.txt /
RUN pip install -r /requirements.txt
ADD app.py /
EXPOSE 5000
CMD python /app.py
