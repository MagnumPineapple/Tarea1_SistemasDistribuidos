FROM python:3.9-slim
RUN apt-get update && apt-get install -y redis-server && apt-get clean
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6379
CMD redis-server & python metrics.py
