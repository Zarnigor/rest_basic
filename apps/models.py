from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, IntegerField, TextField, ForeignKey, CASCADE, ImageField, TextChoices, \
    BooleanField, DateTimeField


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    is_premium = BooleanField(default=False)
    price = IntegerField()
    description = TextField()
    category = ForeignKey('apps.Category', CASCADE)
    created_at = DateTimeField(auto_now=True)


class Image(Model):
    image = ImageField(upload_to='products/', null=True, blank=True)
    product_id = ForeignKey('apps.Product', CASCADE, related_name='images')


class User(AbstractUser):
    class Type(TextChoices):
        MODERATOR = 'moderator', 'Moderator'
        USER = 'user', 'User'
        ADMIN = 'admin', 'Admin'
        MANAGER = 'manager', 'Manager'

    type = CharField(max_length=15, choices=Type.choices, default=Type.MODERATOR)
