from confluent_kafka import Consumer, KafkaError
from json import loads

consumer = KafkaConsumer(
    'crypto-prices',
     bootstrap_servers=['98.81.242.119:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))

from confluent_kafka import KafkaConsumer
from confluent_kafka import KafkaError
consumer.subscribe(['crypto-prices'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
    print(f'Received: {msg.key().decode("utf-8")}: {msg.value().decode("utf-8")}')