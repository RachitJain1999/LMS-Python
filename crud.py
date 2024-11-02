from database import session
from models import Book

def add_book(title , author , isbn , count):
    print('Adding book to db')
    book = Book(title=title,author=author,isbn=isbn,count=count)
    session.add(book)
    session.commit()

def get_book():
    return session.query(Book).all()