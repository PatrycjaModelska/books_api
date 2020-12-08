from django.urls import path

# from rest_framework.routers import DefaultRouter

from books_DRF.views import ( 
    ApiBookListView,
    ApiBookDetailView,
    ApiBookCreateView,
    ApiBookViewSet,
    ApiWarBookUpdate,
    )


urlpatterns = [
    path('books', ApiBookListView.as_view(), name='apibookslist'),
    path('books/<int:pk>', ApiBookDetailView.as_view(), name='apibookdetail'),
    path('books/post', ApiWarBookUpdate.as_view(), name='apibookpost'),
    path('books/create', ApiBookCreateView.as_view(), name='apibookcreate'),
]


# router = DefaultRouter()
# router.register(r'v2/books', ApiBookViewSet, basename='bookviewset')
# urlpatterns += router.urls