from flask_sqlalchemy import SQLAlchemy
from core import app, jsonify, Response
from dataclasses import dataclass

SQL   = SQLAlchemy(app)

@dataclass
class Product(SQL.Model):
    id: int
    title: str
    image: str
    price: str
    overload_create: int
    overload_update: int

    id              = SQL.Column(SQL.Integer, primary_key=True, autoincrement=False)
    title           = SQL.Column(SQL.String(150))
    image           = SQL.Column(SQL.String(250))
    price           = SQL.Column(SQL.String(11))
    overload_create = SQL.Column(SQL.Integer, nullable=False, default=0)
    overload_update = SQL.Column(SQL.Integer, nullable=False, default=0)

    def default():
        return Product.query.all()

    def all():
        return jsonify(Product.query.all())

    def retrieve(pk):
        return jsonify(Product.query.get(pk))

    def response(pk) -> set:
        return str(Response.get_json(jsonify(Product.query.get(pk)))["id"])

    def insert(data) -> set:
        product = Product(id=data['id'], title=data['title'], image=data['image'], price=data['price'])
        SQL.session.add(product)
        SQL.session.commit()

        return f"Producto {data['id']} Id, creado."

    def update(data) -> set:
        product = Product.query.get(data["id"])
        product.title = data["title"]
        product.image = data["image"]
        product.price = data["price"]
        SQL.session.commit()

        return f"Producto {data['id']} Id, actualizado."

    def delete(pk) -> set:
        print(f"El Producto {pk} Id, a sido eliminado.")
        product = Product.query.get(pk)
        SQL.session.delete(product)
        SQL.session.commit()

    def overlayCreate(pk) -> set:
        product = Product.query.get(pk)
        product.overload_create = product.overload_create + 1
        SQL.session.commit()

        return f"El Producto {pk} Id, se ha incrementado en la columna ||overload_create||... +1"

    def overlayUpdate(pk) -> set:
        product = Product.query.get(pk)
        product.overload_update = product.overload_update + 1
        SQL.session.commit()

        return f"El Producto {pk} Id, se ha incrementado en la columna ||overload_update||... +1"
