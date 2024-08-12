from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = 'category',


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',

    def to_representation(self, instance: Category):
        repr = super().to_representation(instance)
        repr['products'] = ProductModelSerializer(instance.product_set.all(), many=True, context=self.context).data
        return repr
