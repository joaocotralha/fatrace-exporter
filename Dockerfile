FROM python:3.9-slim

RUN pip install --no-cache-dir prometheus_client

RUN mkdir /app
COPY exporter.py /app/

RUN apt-get update
RUN apt-get -y install fatrace
WORKDIR /mount

CMD ["python", "/app/exporter.py"]