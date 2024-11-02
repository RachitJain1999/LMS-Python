from datetime import date
from database import session
from models import Book, Member, Transaction

def add_book(title , author , isbn , count):
    book = Book(title=title,author=author,isbn=isbn,count=count)
    session.add(book)
    session.commit()
    print(f"{book.title} is Added")

def get_book():
    return session.query(Book).all()

def add_member(name , email):
    member = Member(name = name , email = email)
    session.add(member)
    session.commit()

def get_members():
    return session.query(Member).all()

def issue_book(book_id,member_id):
    book = session.query(Book).filter_by(id = book_id).first()
    if(book and book.count > 0):
        transaction = Transaction(book_id = book_id,member_id = member_id,issue_date = date.today())
        book.count -= 1
        session.add(transaction)
        session.commit()
        print(f"{book.title} issued")
    else:
        print("Book is not available . Sorry :(")