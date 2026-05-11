from .models import Post
from django_filters import FilterSet


class Filter_News(FilterSet):
    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'title': ['icontains'],
            'date_pub': ['gt'],
        }