# archivo: producer.py
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')  # kafka es el nombre del servicio en k8s

topic_name = 'demo-topic'

def send_messages():
    i = 0
    while True:
        message = f"Mensaje #{i}"
        producer.send(topic_name, value=message.encode('utf-8'))
        print(f"Enviado: {message}")
        producer.flush()
        i += 1
        time.sleep(5)

if __name__ == "__main__":
    send_messages()
