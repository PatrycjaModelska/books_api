import requests

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book, Author, Category
from books_DRF.serializers import BookListSerializer, BookCreatSerializer
from books_DRF.googleapis import get_google_apis


class ApiBookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class ApiBookDetailView(generics.RetrieveAPIView):
    """
    Returns details for one book
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class ApiBookCreateView(generics.CreateAPIView):
	"""
    Returns details for one book
    """
	queryset = Book.objects.all()
	serializer_class = BookCreatSerializer


class ApiWarBookUpdate(APIView):
	"""
    Adds or updates books in the database
    """
	def post(self, request, format=None):
		books = get_google_apis(request.data.get("q"))

		added_books = 0
		updated_books = 0
		
		for book in books:
			bookinfo = book.get('volumeInfo', {})
			book_object = Book.objects.filter(title=bookinfo.get('title'),
											  published_date=bookinfo.get("publishedDate")).first()

			if not book_object:
				new_book = Book(title=bookinfo.get('title'),
								published_date=bookinfo.get("publishedDate"),
								average_rating=bookinfo.get("averageRating"),
								ratings_count=bookinfo.get("ratingsCount"),
								thumbnail=bookinfo.get("imageLinks", {}).get("thumbnail"),
								)
				new_book.save()

				for author in bookinfo.get('authors', []):
					obj, created = Author.objects.get_or_create(name=author)
					new_book.authors.add(obj)

				for category in bookinfo.get('categories', []):
					obj, created = Category.objects.get_or_create(name=category)
					new_book.categories.add(obj)

				added_books += 1

			else:
				book_object.published_date = bookinfo.get("publishedDate")
				book_object.average_rating = bookinfo.get("averageRating")
				book_object.ratings_count = bookinfo.get("ratingsCount")
				book_object.thumbnail = bookinfo.get("imageLinks", {}).get("thumbnail")
				book_object.save(update_fields=('published_date', 'average_rating', 'ratings_count', 'thumbnail',))

				updated_books += 1

		return Response(
			{'received data': f'You added {added_books} new, and updated {updated_books} already existing books.'})


# ModelViewSet example

class ApiBookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
