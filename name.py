
from crud import add_book, get_book
def main():
    print("***********************************")
    print('1. Add Book')
    print('2. All Books')
    print("***********************************")

    choice = input("Enter your Choice: ")

    if(choice == '1'):
        title = input('Enter Title: ')
        author = input('Enter book author: ')
        isbn = input('Enter book ISBN: ')
        count = int(input('Enter number of Copies: '))
        add_book(title , author , isbn , count)

    elif(choice == '2'):
        print('++++ ALl Books ++++')
        books = get_book()
        for book in books:
            isAvailable = "Available" if book.count > 0 else "Not Available"
            print(f"Id : {book.id}")
            print(f"Title : {book.title}")
            print(f"Author : {book.author}")
            print(f"ISBN : {book.isbn}")
            print(f"Copies Available : {book.count}")
            print(f"{isAvailable}")

            print('-------------------------------')

if(__name__ == "__main__"):
    main()