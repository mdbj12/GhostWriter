from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    all = []

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)
    fav_genre = Column('favorite genre', String)
    email = Column('email', String)
    phone_number = Column('phone number', Integer)

    def __repr__(self):
        return f"""
                name: {self.name},
                age:{self.age},
                fav_genre:{self.fav_genre},
                email:{self.email},
                phone_number:{self.phone_number}
                """
    

class Books(Base):
    __tablename__ = 'books'

    all = []

    id = Column(Integer(), primary_key=True)
    title = Column('title', String())
    author = Column('author', String())
    publish_date = Column('date', String())
    read = Column('read', Boolean())

    def __init__(self, title, author, publish_date, read):
        self.title = title
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