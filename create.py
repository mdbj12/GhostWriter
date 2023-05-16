from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

from models import Base, User, Books, Reviews
import click
import keyboard

print(f'''
  (`\ .-') /`  ('-.          .-')   .-') _    ('-.  ('-.                                                      _  .-')                     .-') _                       
   `.( OO ),'_(  OO)        ( OO ).(  OO) ) _(  OO)( OO ).-.                                                 ( \( -O )                   ( OO ) )                      
,--./  .--. (,------.      (_)---\_/     '.(,------/ . --. /,--.             ,--.   ,--.-'),-----. ,--. ,--.  ,------.         ,-.-'),--./ ,--,'   ,------..-'),-----. 
|      |  |  |  .---'      /    _ ||'--...__|  .---| \-.  \ |  |.-')          \  `.'  ( OO'  .-.  '|  | |  |  |   /`. '        |  |OO|   \ |  |\('-| _.---( OO'  .-.  '
|  |   |  |, |  |          \  :` `.'--.  .--|  | .-'-'  |  ||  | OO )       .-')     //   |  | |  ||  | | .-')|  /  | |        |  |  |    \|  | (OO|(_\   /   |  | |  |
|  |.'.|  |_(|  '--.        '..`''.)  |  | (|  '--\| |_.'  ||  |`-' |      (OO  \   / \_) |  |\|  ||  |_|( OO |  |_.' |        |  |(_|  .     |//  |  '--.\_) |  |\|  |
|         |  |  .--'       .-._)   \  |  |  |  .--'|  .-.  (|  '---.'       |   /  /\_  \ |  | |  ||  | | `-' |  .  '.'       ,|  |_.|  |\    | \_)|  .--'  \ |  | |  |
|   ,'.   |  |  `---.      \       /  |  |  |  `---|  | |  ||      |        `-./  /.__)  `'  '-'  ('  '-'(_.-'|  |\  \       (_|  |  |  | \   |   \|  |_)    `'  '-'  '
'--'   '--'  `------'       `-----'   `--'  `------`--' `--'`------'          `--'         `-----'  `-----'   `--' '--'        `--'  `--'  `--'    `--'        `-----' 
''')
print(f'''
loading books....
generating user....
compiling data....
''')
      
engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


user_input = input('Ready to get your data stolen? Y/n: ')
if user_input.lower() == 'y':
    @click.command()
    @click.option('--name', prompt='Enter name')
    @click.option('--age', prompt='Enter age')
    @click.option('--fav_genre', prompt='Enter favorite genre')
    @click.option('--email', prompt='Enter email')
    @click.option('--phone_number', prompt='Enter phone number')

    def create_user(name,age,fav_genre,email,phone_number):
        new_user = User(
            name=name,
            age=age,
            fav_genre=fav_genre,
            email=email,
            phone_number=phone_number
            )

        session.add(new_user)
        session.commit()

    if __name__ == '__main__':
        create_user()    
else:
    print('Too bad I couldnt steal your data')

book = input('Do you want to add a new book? Y/n: ')
if book.lower() == 'y':
    @click.command()
    @click.option('--title', prompt='Enter Title')
    @click.option('--author', prompt='Enter Author')
    @click.option('--publish_date', prompt='Enter Publish_Date (MMDDYYYY format)')
    @click.option('--read', prompt='Have you read this book?')

    def add_book(title, author, publish_date, read):
        new_book = Books(
            title=title,
            author=author,
            publish_date=publish_date,
            read=read
            )

        session.add(new_book)
        session.commit()

    if __name__ == '__main__':
        add_book()
    else:
        print('Read more books!')
