# archivo: consumer.py
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'demo-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='demo-consumer-group'
)

if __name__ == "__main__":
    print("Esperando mensajes...")
    for message in consumer:
        print(f"Recibido: {message.value.decode('utf-8')}")
