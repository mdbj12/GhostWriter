from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapped_column

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    all = []

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)
    fav_genre = Column('favorite genre', String)
    email = Column('email', String)

    def __repr__(self):
        return f"""
                id: {self.id}
                name: {self.name},
                age:{self.age},
                fav_genre:{self.fav_genre},
                email:{self.email}
                """
    

class Book(Base):
    __tablename__ = 'books'

    all = []

    id = Column(Integer(), primary_key=True)
    title = Column('title', String())
    author = Column('author', String())
    
    reviews = relationship("Review", back_populates="book")
    
    def __repr__(self):
        return f"""
                id: {self.id},
                title: {self.title},
                author:{self.author}
                """

        Book.all.append(self)

class Review(Base):
    __tablename__ = 'reviews'

    all = []

    id = Column(Integer(), primary_key=True)
    user_id=Column(Integer())
    book_title=Column(String())
    book_author=Column(String())
    book_id=Integer()
    text = Column('review', String())
    rating = Column('rating out of 5', Integer())
    

    book = relationship("Book", back_populates="reviews")
    
    # books = ForeignKey("books")
    
    book_id= mapped_column(ForeignKey("books.id"))
    # book_title=mapped_column(ForeignKey("books.title"))

    def __repr__(self):
        return f"""
                user_id=Column(Integer())
                book_title:{self.book_title}
                book_author:{self.book_author},
                book_id:{self.book_id}
                rating:{self.rating},
                text: {self.text},
                """
        
        Review.all.append(self)

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)