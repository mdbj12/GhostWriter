from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from models import User

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind = engine)
    session = Session()

    user = User(
        name = 'Michael',
        age = 22,
        fav_genre = 'Romance',
        email = 'exmaple@example.com',
        phone_number = 911
    )

    session.add(user)
    session.commit()