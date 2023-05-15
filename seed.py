from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# from models import User

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind = engine)
    session = Session()

#     u1 = User(
#         name = 'Michael',
#         age = 22,
#         fav_genre = 'Romance',
#         email = 'exmaple@example.com',
#         phone_number = 911
#     )
#     u2 = User(
#         name = 'Ian',
#         age = 20,
#         fav_genre = 'Romance',
#         email = 'exmaple@example.com',
#         phone_number = 111
#     )
#     u3 = User(
#         name = 'Wicheal',
#         age = 24,
#         fav_genre = 'Romance',
#         email = 'exmaple@example.com',
#         phone_number = 211
#     )

#     users = [u1, u2 , u3]

#     session.add_all(users)
#     session.commit()