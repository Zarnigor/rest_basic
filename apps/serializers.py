from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, Image


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = 'created_at',
        exclude = ()

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['images'] = ImageModelSerializer(instance.images.all(), many=True, context=self.context).data
        return repr


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',

    # def to_representation(self, instance: Category):
    #     repr = super().to_representation(instance)
    #     repr['products'] = ProductModelSerializer(instance.product_set.all(), many=True, context=self.context).data
    #     return repr


class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = Image
        exclude = ()
