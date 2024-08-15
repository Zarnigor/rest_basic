from django.db.models import Count
from django_filters import FilterSet, BooleanFilter, ChoiceFilter

from apps.models import Category, Product


class CategoryFilterSet(FilterSet):
    class Meta:
        model = Category
        fields = ['name']


class ProductFilterSet(FilterSet):
    image = BooleanFilter(method='has_image')

    class Meta:
        model = Product
        fields = ['is_premium']

    def has_image(self, queryset, field, value):
        if value:
            return queryset.annotate(product_icount=Count('images')).filter(product_icount__gte=1)

        return queryset
