# RABBITMQ { conexiones }
import pika, json
from models import Product, app

# URL { params }
params = pika.URLParameters("<URLParameters:: Cloud RabbitMQ>")

# Conexion de bloqueo Pika
connection = pika.BlockingConnection(params)

# Canal para publicacion
channel = connection.channel()

# Conexión directa { Main }
channel.queue_declare(queue="backup")

# Consumidor { ++CPU }
def subscriber(ch, method, properties, body):
    # Encode { Json }
    data = json.loads(body)

    with app.app_context():
        if properties.content_type == "created":
            try:
                if str(data["id"]) == Product.response(pk=data["id"]):
                    # Query Id { database }
                    print(
                        f"El Producto {data['id']} Id, a sido registrado anteriormente..."
                    )
                    # DDL Insert { ruling }
                    print(Product.overlayCreate(pk=data["id"]))
            except BaseException:
                # DML { Insert }
                print(Product.insert(data=data))

        elif properties.content_type == "updated":
            try:
                if str(data["id"]) == Product.response(pk=data["id"]):
                    # DML { Update }
                    print(Product.update(data=data))
                    # DML Insert { Rule_Update }
                    print(Product.overlayUpdate(pk=data["id"]))
            except BaseException:
                # Query Id { database }
                print(
                    f"El Id ||{data['id']}|| no se encuentra en la Base de datos, por lo tanto no se actualizara..."
                )
        elif properties.content_type == "deleted":
            try:
                if str(data["id"]) == Product.response(pk=data["id"]):
                    # Query Id { database }
                    Product.delete(pk=data["id"])
            except BaseException:
                print(
                    f"El Producto {data['id']} Id no se encuentra registrado en la Base de datos..."
                )
        else:
            print("-- CPU { Error }")


# Consumo basico del canal
channel.basic_consume(queue="backup", on_message_callback=subscriber, auto_ack=True)

print("RabbitMQ Main en Producción { ./data/main.py }")

# Consumir el canal
channel.start_consuming()

# Cerramos el canal
channel.close()
