import django_filters
from .models import Letter

class LetterFilter(django_filters.filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Letter
        fields = ['recipient']