from django.urls import path

from books.views import (
    homepage,
    BookDetailView,
    BooksListView,
    books_import,
    )


urlpatterns = [
    path('', homepage , name="homepage"),
    path('book/<int:pk>/', BookDetailView.as_view(), name='bookdetailview'),
    path('books/', BooksListView.as_view(), name='bookslist'),
    path('db/', books_import, name='booksimport'),
]
