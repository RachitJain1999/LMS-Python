from datetime import date
from database import session
from models import Book, Member, Transaction


def get_transactions_by_member(member_id):
    return session.query(Transaction).filter_by(member_id = member_id).all()

def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book and book.count > 0:
        # session.delete(book)
        book.count = 0
        session.commit()
        print("> Books in stock deleted")
    else:
        print("> Book not in stock: ", book_id)
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

def return_book(transactioId):
    transaction = session.query(Transaction).filter_by(id = transactioId).first()
    if(transaction and not transaction.return_date):
        transaction.return_date = date.today()
        book = session.query(Book).filter_by(id = transaction.book_id).first()
        book.count += 1
        session.commit()    
        print('Book returned to Library :)')
    else:
        print(' > Book already returned :)')

def tnByMem(memberId):
    getTransactionForMember()