FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y vim && apt-get clean
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY producer.py .
CMD ["python3", "producer.py"]
