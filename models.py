from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

#creating user class table. importing this class to create.py component
class User(Base):
    __tablename__ = 'users'

    all = []

    #defining which columns will be storing what specific type of data.
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)
    fav_genre = Column('favorite genre', String)

    #column layout and what inputs it will take in
    def __repr__(self):
        return f'''
            id: {self.id}
            name: {self.name},
            age:{self.age},
            fav_genre:{self.fav_genre},
        '''
    
#careting books class table, importing this to create.py
class Books(Base):
    __tablename__ = 'books'

    all = []

    #the columns generated into the table with what type of data value it will take in
    id = Column(Integer(), primary_key=True)
    title = Column('title', String())
    author = Column('author', String())
    read = Column('read', Boolean())

    #column layout and the input will be whatever the user puts in
    def __repr__(self):
        return f'''
            id: {self.id},
            title: {self.title},
            author: {self.author},
            read: {self.read}
        '''

#creating reviews class table, importing this to create.py
class Reviews(Base):
    __tablename__ = 'reviews'

    all = []

    #the columns generated for the reviews table, also declaring what type of data will be allowed to be input
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    book_id = Column(Integer(), ForeignKey('books.id'))
    book_title = Column('book title', String())
    book_author = Column('book author', String())
    review = Column('review', String())
    rating = Column('rating out of 5', Integer())

    #column layout will be filled with whatever user inputs for each specific column
    def __repr__(self):
        return f'''
            id: {self.id},
            user_id: {self.user_id},
            book_id: {self.book_id},
            book_title: {self.book_title},
            book_author: {self.book_author},
            review: {self.review},
            rating: {self.rating}
        '''

#creates the association from python to sql
if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)