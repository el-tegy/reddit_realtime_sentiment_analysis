from json import dumps

from kafka import KafkaProducer


def get_kafka_producer():
    try:
        return KafkaProducer(
            bootstrap_servers=['kafkaservice:9092'],
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
    except Exception as e:
        print('An error occurred: {e}')
