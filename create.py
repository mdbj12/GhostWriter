from sqlalchemy import create_engine, update, ForeignKey
from sqlalchemy.orm import sessionmaker, mapped_column

from models import Base, User, Book, Review
import click
import keyboard

# def create_user(users):
#     with open('app.db', 'w') as gr:
#         for user in users:
#              gr.write(user)
# @click.command()
# @click.option('--name', prompt='Enter name')
# @click.option('--age', prompt='Enter age')
# @click.option('--fav_genre', prompt='Enter favorite genre')
# @click.option('--email', prompt='Enter email')
# @click.option('--phone_number', prompt='Enter phone number')

# @click.option('--createbook', prompt='Welcome! Create new book? Y or N')
print(f'''
loading books....
generating user....
loading reviews....
compiling data....
''')
      
engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

options = 0
while options != 6:
    print('')
    print('(1) Let me steal your data!')
    print('(2) Want to add a book?')
    print('(3) Write a review?')
    print('(4) Wanna see who read the most books?')
    print('(5) Wanna see which book has the most reviews?')
    print('(6) QUIT now before I steal your data!!!')

    options = int(input())

    if options == 1:
        def create_user():

            name=input("Name:")
            age=input("Age:")
            fav_genre=input("Favorite genre:")
            email=input("Email:")
            new_user  = User(name=name,age=age,fav_genre=fav_genre, email=email)
            session.add(new_user)
            session.commit()
            print("")
            print(f"New user registered! Your unique user ID is {new_user.id}.")

        if __name__ == '__main__':
            create_user()
        continue

    elif options == 2:
        def create_book():
            title=input("Title")
            author=input("Author")
            new_book = Book(title=title,author=author)

            session.add(new_book)
            session.commit()
            print(f"Submitted! Your updated books list: {session.query(Book).all()}")
           
        if __name__ == '__main__':
                create_book()
        continue

    elif options == 3:

        def create_review():

            userid = input("Enter your unique user ID!")

            books=session.query(Book).all()
            users=session.query(User).all()

            user_ids=[]
            for user in users:
                user_ids.append(user.id)

        

            while int(userid) not in user_ids:
                userid= input(f'Please enter valid user id! Registered users: {users} ')
            
            
            user=session.query(User).filter_by(id=userid).first()
            if user is not None:
                user_name=user.name
            print(f"")
            print(f"Welcome, {user.name}!!")
            print(f"")
            print("To start your review, enter a book's ID or search by title and author!")
            
            search_options = 0
            # # while search_options != 1 or 2 :
            #     print('')
            print('(1) Enter book ID')
            print('(2) Search by title and author')
            search_options = int(input())

            if search_options == 1:
                print("")
                book_ids=[]
                for book in books:
                    book_ids.append(book.id)

                print(f"Book Options: {books}")
                bookid = input("Enter book ID: ")
                
                while int(bookid) not in book_ids:
                    bookid = input(f'ERROR: Please enter a valid book ID! \n Valid book IDs: {book_ids} ')

                
                book = session.query(Book).filter_by(id=bookid).first()
                if book is not None:
                    booktitle = book.title
                    bookauthor = book.author

                rating = input(f"How would you rate {booktitle} by {bookauthor} out of 10? ")
                text = input(f"Leave a review for {booktitle}! ")
            
                new_review= Review(user_id=userid, text=text, rating=rating, book_id=bookid, book_title=booktitle, book_author=bookauthor)

                # session.add(new_review)
                # session.commit()
            

            elif search_options == 2:
                book_titles=[]
                # book_authors=[]
                for book in books:
                    book_titles.append(book.title)
                    # book_authors.append(book.author)

                booktitle=input("Enter book title: ")

                while booktitle not in book_titles:
                    booktitle = input(f'ERROR: Please enter a valid book title! \n Valid book titles: {book_titles} ')
                
                authors=[]
                for book in books:
                    if booktitle == book.title:
                        authors.append(book.author)
                
                authors_list=[]
                author_numbers=[]
                for i in range (len(authors)):
                    authors_list.append(f'{i+1}: {authors[i]}')
                    author_numbers.append(i+1)


                author_option = int(input(f"Title found! Now select the number corresponding to its author \n {authors_list} "))
                    
                while author_option not in author_numbers:
                    print(author_numbers)
                    author_option = int(input(f'ERROR: Please select a valid number! \n Valid numbers: {authors_list} '))
                    
                rating = input(f"How would you rate {booktitle} by {authors[author_option-1]} out of 5? ")
                text = input(f"Leave a review for {booktitle} by {authors[author_option-1]}! ")

                book = session.query(Book).filter_by(title=booktitle).filter_by(author=authors[author_option-1]).first()
                # book_by_title_and_author = book_by_title.filter_by(author=authors[author_option-1]).first()
                bookid = book.id
                
                if book is not None:
                    bookid = book.id

                new_review= Review(user_id=userid, text=text, rating=rating, book_id = bookid,  book_title=booktitle, book_author=authors[author_option-1])

            session.add(new_review)
            print ("Review submitted!")
            session.commit()
                

        if __name__ == '__main__':
            create_review()
        continue
        
        

    

    