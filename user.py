from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_user(client_inputs):
    # print("creating engine")
    engine = create_engine('sqlite:///users.db')
    # print("engine created – creating session")
    session = sessionmaker(bind=engine)()
    # print("session created – creating new user")
    new_user = User(name=client_inputs[0], age=client_inputs[1])
    # print("created user – adding user to session")
    session.add(new_user)
    # print("added user to session – committing changes to SQLite")
    session.commit()
    # return print("yay")

if __name__ == '__main__':
    user = []

    name = input("username: ")
    age = input("age: ")

    user.append(name)
    user.append(age)

    create_user(user)