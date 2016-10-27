FROM python:3.5
MAINTAINER Skablam
ADD requirements.txt /
RUN pip install -r /requirements.txt
RUN mkdir /code
WORKDIR /code
CMD python /code/app.py
