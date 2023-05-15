from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    all = []

    id = Column(Integer(), primary_key=True)
    name = Column('name', String())
    age = Column('age', Integer())
    fav_genre = Column('favorite genre', String())
    email = Column('email', String())
    phone_number = Column('phone number', Integer())

    def __init__(self, name, age, fav_genre, email, phone_number):
        self.name = name
        self.age = age
        self.fav_genre = fav_genre
        self.email = email
        self.phone_number = phone_number

        User.all.append(self)

class Books(Base):
    __tablename__ = 'books'

    all = []

    id = Column(Integer(), primary_key=True)
    name = Column('name', String())
    author = Column('name', String())
    publish_date = Column('date', String())
    read = Column('read', Boolean())

    def __init__(self, name, author, publish_date, read):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.read = read

        Books.all.append(self)

class Reviews(Base):
    __tablename__ = 'reviews'

    all = []

    id = Column(Integer(), primary_key=True)
    text = Column('review', String())
    rating = Column('rating out of 5', Integer())

    def __init__(self, text, rating):
        self.text = text
        self.rating = rating

        Reviews.all.append(self)

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)