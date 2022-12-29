from flask import Flask, jsonify, Response
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Config { db }
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///backup.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/", methods=["GET"])
def core():
    from models import Product

    return Product.all()


@app.route("/<int:id>", methods=["GET"])
def query(id):
    from models import Product

    try:
        if str(id) in Product.response(pk=id):
            return Product.retrieve(pk=id)
    except TypeError:
        return f"El producto {id} No se encuentra en la Base de datos"


@app.route("/product", methods=["GET"])
def overlayProducts():
    from schemas import Schemas

    return Schemas.overlayProducts()


@app.route("/product/overlay-create", methods=["GET"])
def overlayCreate():
    from schemas import Schemas

    return Schemas.overlayCreate()


@app.route("/product/overlay-update", methods=["GET"])
def overlayUpdate():
    from schemas import Schemas

    return Schemas.overlayUpdate()


# On { Server }
if __name__ == "__main__":
    # SqlAlchemy
    from models import SQL

    # On
    SQL.init_app(app)

    # On
    app.run(debug=True)
