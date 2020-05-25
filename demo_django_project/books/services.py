from .models import Book

class BookService:   
    
    def like(book_id):
        book = Book.objects.get(id=book_id)
        book.nb_likes = book.nb_likes + 1
        book.save()