import django_filters
from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, Author


class PostFilter(FilterSet):
    author = django_filters.ModelMultipleChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'time_in': ['date__gte']
            }


