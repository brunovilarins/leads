FROM python:3.8.5

RUN mkdir /leads
VOLUME /leads

WORKDIR /leads

COPY . /
RUN chmod +x /entrypoint.sh

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

