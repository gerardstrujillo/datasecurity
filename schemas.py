from core import app, Marshmallow
from models import Product

serializer = Marshmallow(app)

class Products(serializer.Schema):
    class Meta:
        fields = ('id','title', 'image', 'price')

class OverloadCreate(serializer.Schema):
    class Meta:
        fields = ('id','overload_create')

class OverloadUpdate(serializer.Schema):
    class Meta:
        fields = ('id','overload_update')

# Schemas { Json }
class Schemas:
    def overlayCreate():
        content = OverloadCreate(many=True)
        return content.jsonify(Product.default())

    def overlayUpdate():
        content = OverloadUpdate(many=True)
        return content.jsonify(Product.default())

    def overlayProducts():
        content = Products(many=True)
        return content.jsonify(Product.default())