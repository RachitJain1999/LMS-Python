
from crud import add_book, add_member, get_book, get_members
def main():
    print("***********************************")
    print('1. Add Book')
    print('2. All Books')
    print('3. Add Member')
    print('4. View Membes')
    print('5. Issue Book')
    print('6. Return Book')
    print('7. View Transactions by Member')
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

    elif(choice == '3'):
        name=input("Enter Member Name: ")
        email = input("Enter Email: ")
        add_member(name,email)
        print(f"{name} added Successfully. Congratulations")
    
    elif(choice == '4'):
        members = get_members()
        print('***** All Members ******8')
        for member in members:
            print(f"Member Name : {member.name}")
            print(f"Email : {member.email}")
            print('-------------------------------')
        

    elif(choice == 5):
        pass

    elif(choice == 6):
        pass

    elif(choice == 7):
        pass
    

if(__name__ == "__main__"):
    main()