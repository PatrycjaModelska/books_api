import django_filters
from .models import Book, Author


class BookFilter(django_filters.FilterSet):

	CHOICES = (
			('ascending', 'Ascending'),
			('descending', 'Descending')
		)

	ordering = django_filters.ChoiceFilter(label='published date ordering', 
		choices=CHOICES, method='published_date_ordering')

	published_date = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Book
		fields = ('authors', 'published_date')

	def published_date_ordering(self, queryset, name, value):
		expression = 'published_date' if value == 'ascending' else '-published_date'
		return queryset.order_by(expression)
