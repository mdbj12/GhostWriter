from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'User'

    all = []

    id = Column(Integer(), primary_key=True)
    name = Column('Name', String())
    age = Column('Age', Integer())
    fav_genre = Column('Favorite Genre', String())
    email = Column('Email', String())
    phone_number = Column('Phone Number', Integer())

    def __init__(self, name, age, fav_genre, email, phone_number):
        self.name = name
        self.age = age
        self.fav_genre = fav_genre
        self.email = email
        self.phone_number = phone_number

        User.all.append(self)

