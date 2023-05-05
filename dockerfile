FROM python:3.8-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 


