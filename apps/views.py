from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.filters import CategoryFilterSet, ProductFilterSet
from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


@extend_schema(tags=["category"])
class CategoryListCreateAPIView(ListCreateAPIView):  # get post
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    # filterset_fields = 'name'
    filterset_class = CategoryFilterSet


@extend_schema(tags=["category"])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=["product"])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filterset_class = ProductFilterSet
