from django.urls import path

from apps.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, ProductListCreateAPIView

urlpatterns = [
    path('categories', CategoryListCreateAPIView.as_view()),
    path('products', ProductListCreateAPIView.as_view()),
    path('category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view()),
]