from django.db.models import CharField, Model, IntegerField, TextField, ForeignKey, CASCADE, ImageField


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    title = CharField(max_length=255)
    price = IntegerField()
    description = TextField()
    category = ForeignKey('apps.Category', CASCADE)
    image = ImageField(upload_to='products/')
