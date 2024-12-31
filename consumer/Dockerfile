FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y vim && apt-get clean
COPY consumer.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "./consumer.py" ]
