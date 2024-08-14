from django.db.models import CharField, Model, IntegerField, TextField, ForeignKey, CASCADE, ImageField


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField()
    description = TextField()
    category = ForeignKey('apps.Category', CASCADE)

class Image(Model):
    image = ImageField(upload_to='products/', null=True, blank=True)
    product_id = ForeignKey('apps.Product', CASCADE, related_name='images')