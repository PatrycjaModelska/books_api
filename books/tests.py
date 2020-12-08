from django.test import TestCase
from django.shortcuts import reverse


class HelloViewTests(TestCase):
	def test_bookslist_page(self):
		response = self.client.get(reverse("bookslist"))
		self.assertEqual(response.status_code, 200)

	def test_booksimport_page(self):
		response = self.client.get(reverse("booksimport"))
		self.assertEqual(response.status_code, 200)
