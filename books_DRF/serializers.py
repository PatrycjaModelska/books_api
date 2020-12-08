from rest_framework import serializers

from books.models import Book, Author, Category


class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        return str(value)


class BookListSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """

    #return only id
    # categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    # authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())

    #return representation 
    categories = MyPrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    authors = MyPrimaryKeyRelatedField(many=True, queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id','title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count', 'thumbnail'] #order in which the fields are displayed
        depth = 1


class BookCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = Author
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    """
    Serializing all the categories
    """
    class Meta:
        model = Category
        fields = '__all__'


