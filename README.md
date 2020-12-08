# REST API DJANGO
## War books
### Functionalities

* GET /books - list of all books in database with filters: /books?published_date=1995, /books?sort=-published_date
* GET /books?author="Jan Kowalski"&author="Anna Kowalska" - another filters
* GET /books/<bookId> - book ditails
* POST /db  with body {"q": "war"} - loading data form https://www.googleapis.com/books/v1/volumes?q=war
(updating existing data)
   
 
### Deployment
    
You can see project here: https://war-books.herokuapp.com/books
