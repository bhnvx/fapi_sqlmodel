import pika
from ..config import *


def send_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=Message_Host)
    )
    channel = connection.channel()
    channel.queue_declare(queue=Message_Queue)

    # TODO : Data Send Logic

    channel.basic_publish(exchange='', routing_key=Message_Key, body='')
    connection.close()