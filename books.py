from models import Books
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_books(client_inputs):
    engine = create_engine('sqlite:///users.db')
    session = sessionmaker(bind=engine)()
    new_user = Books(
        title=client_inputs[0],
        author=client_inputs[1],
        publish_date=client_inputs[2],
    )
    session.add(new_user)
    session.commit()

if __name__ == '__main__':
    book = []

    title = input('Book Title: ')
    author = input('Book Author: ')
    publish_date = input('Date (MMDDYYY format): ')

    book.append(title)
    book.append(author)
    book.append(publish_date)

    create_books(book)
