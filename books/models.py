from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=25600)

	def __str__(self):
		return '{}'.format(self.name)


class Category(models.Model):
	name = models.CharField(max_length=25600)

	def __str__(self):
		return '{}'.format(self.name)


class Book(models.Model):
	title = models.CharField(max_length=25600)
	authors = models.ManyToManyField(Author)
	published_date = models.CharField(max_length=25600, null=True)
	categories = models.ManyToManyField(Category)
	average_rating = models.IntegerField(null=True)
	ratings_count = models.IntegerField(null=True)
	thumbnail = models.CharField(max_length=25600, null=True)

	def __str__(self):
		return '{}'.format(self.title)