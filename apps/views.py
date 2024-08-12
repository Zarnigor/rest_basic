from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.models import Category
from apps.serializers import CategoryModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView): #get post
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
