import requests


def get_google_apis(q):
	response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={q}')
	if response.status_code == 200:
		data = response.json()
		books = data.get('items', [])
		return books