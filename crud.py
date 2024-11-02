from database import session
from models import Book, Member

def add_book(title , author , isbn , count):
    print('Adding book to db')
    book = Book(title=title,author=author,isbn=isbn,count=count)
    session.add(book)
    session.commit()

def get_book():
    return session.query(Book).all()

def add_member(name , email):
    member = Member(name = name , email = email)
    session.add(member)
    session.commit()

def get_members():
    return session.query(Member).all()
