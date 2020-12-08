import requests

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Book, Author, Category
from .filters import BookFilter
from books_DRF.googleapis import get_google_apis


def homepage(request):
    return render(request, 'homepage.html')


class BookDetailView(DetailView):
    model = Book
    template_name = 'bookdetail.html'


def books_import(request):
    if request.method == "POST":
        books = get_google_apis(request.POST.get("q"))

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

            else:
                book_object.published_date = bookinfo.get("publishedDate")
                book_object.average_rating = bookinfo.get("averageRating")
                book_object.ratings_count = bookinfo.get("ratingsCount")
                book_object.thumbnail = bookinfo.get("imageLinks", {}).get("thumbnail")
                book_object.save(update_fields=('published_date', 'average_rating', 'ratings_count', 'thumbnail',))

        return redirect('bookslist')
    else:
        return render(request, 'booksimport.html')


class BooksListView(ListView):
    model = Book
    template_name = 'bookslist.html'
    ordering = ['title']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context
