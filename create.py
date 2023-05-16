from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

from models import Base, User, Books, Reviews
import click

# def create_user(users):
#     with open('app.db', 'w') as gr:
#         for user in users:
#              gr.write(user)
@click.command()
@click.option('--name', prompt='Enter name')
@click.option('--age', prompt='Enter age')
@click.option('--fav_genre', prompt='Enter favorite genre')
@click.option('--email', prompt='Enter email')
@click.option('--phone_number', prompt='Enter phone number')

def create_user(name,age,fav_genre,email,phone_number):
    # print("name {} age {}".format(name, age))
    new_user  = User(name=name,age=age,fav_genre=fav_genre, email=email, phone_number=phone_number)
    
    engine = create_engine("sqlite:///app.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(new_user)
    session.commit()


# def create_book(title,author,publish_date,read)

if __name__ == '__main__':
    create_user()
    # @click.option('--createbook', prompt='Welcome! Create new book? Y or N')
    