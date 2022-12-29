import pika, json

params = pika.URLParameters("<URLParameters:: Cloud RabbitMQ>")

# Conexion de bloqueo Pika
connection = pika.BlockingConnection(params)

# Canal para publicacion
channel = connection.channel()

# Producer Data
def published(method, body):
    # Metadatos { Propiedad del mensaje de cola }
    properties = pika.BasicProperties(method)

    # Parametro: intercambio, clave de enrutamiento para enviar los eventos
    channel.basic_publish(
        exchange="", routing_key="main", body=json.dumps(body), properties=properties
    )
