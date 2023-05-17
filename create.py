from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

from models import Base, User, Books, Reviews
import click

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
loading reviews....
compiling data....
''')
      
engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

options = 0
while options != 4:
    print('(1) Let me steal your data!')
    print('(2) Want to add a book?')
    print('(3) Write a review?')
    print('(4) QUIT now before I steal your data!!!')

    options = int(input())

    if options == 1:
        print('''
                                (`-.     ('-.         _   .-')      ('-.                                           _  .-')         _ .-') _    ('-.    .-') _     ('-.   ,---. 
                              _(OO  )_ _(  OO)       ( '.( OO )_  _(  OO)                                         ( \( -O )       ( (  OO) )  ( OO ).-(  OO) )   ( OO ).-|   | 
         ,----.    ,-.-'),--(_/   ,. (,------.       ,--.   ,--.(,------.        ,--.   ,--.-'),-----. ,--. ,--.  ,------.        \     .'_  / . --. /     '._  / . --. |   | 
        '  .-./-') |  |OO\   \   /(__/|  .---'       |   `.'   | |  .---'         \  `.'  ( OO'  .-.  '|  | |  |  |   /`. '       ,`'--..._) | \-.  \|'--...__) | \-.  \|   | 
        |  |_( O- )|  |  \\   \ /   / |  |           |         | |  |           .-')     //   |  | |  ||  | | .-')|  /  | |       |  |  \  .-'-'  |  '--.  .--.-'-'  |  |   | 
        |  | .--, \|  |(_/ \   '   /,(|  '--.        |  |'.'|  |(|  '--.       (OO  \   / \_) |  |\|  ||  |_|( OO |  |_.' |       |  |   ' |\| |_.'  |  |  |   \| |_.'  |  .' 
       (|  | '. (_,|  |_.'  \     /__)|  .--'        |  |   |  | |  .--'        |   /  /\_  \ |  | |  ||  | | `-' |  .  '.'       |  |   / : |  .-.  |  |  |    |  .-.  `--'  
        |  '--'  (_|  |      \   /    |  `---.       |  |   |  | |  `---.       `-./  /.__)  `'  '-'  ('  '-'(_.-'|  |\  \        |  '--'  / |  | |  |  |  |    |  | |  .--.  
         `------'  `--'       `-'     `------'       `--'   `--' `------'         `--'         `-----'  `-----'   `--' '--'       `-------'  `--' `--'  `--'    `--' `--'--' 
        ''')
        @click.command()
        @click.option('--name', prompt='Enter name: ')
        @click.option('--age', prompt='Enter age: ')
        @click.option('--fav_genre', prompt='Enter favorite genre: ')
        @click.option('--email', prompt='Enter email: ')
        @click.option('--phone_number', prompt='Enter phone number: ')

        def create_user(name,age,fav_genre,email,phone_number):
            new_user = User(
                name = name,
                age = age,
                fav_genre = fav_genre,
                email = email,
                phone_number = phone_number
                )
            session.add(new_user)
            session.commit()

        if __name__ == '__main__':
            create_user.main(standalone_mode=False)
        else:
            print('Too bad I couldnt steal your data...')
        continue

    elif options == 2:
        print('''
       (`\ .-') /`('-. .-.  ('-.    .-') _          _ .-') _         _ .-') _                                                   _  .-')    ('-.  ('-.    _ .-') _  ,------.  
        `.( OO ),( OO )  / ( OO ).-(  OO) )        ( (  OO) )       ( (  OO) )                                                 ( \( -O ) _(  OO)( OO ).-( (  OO) )'  .--.  ' 
        ,--./  .--. ,--. ,--. / . --. /     '._        \     .'_  ,-.-')\     .'_         ,--.   ,--.-'),-----. ,--. ,--.          ,------.(,------/ . --. /\     .'_|  |  |  | 
        |      |  | |  | |  | | \-.  \|'--...__)       ,`'--..._) |  |OO,`'--..._)         \  `.'  ( OO'  .-.  '|  | |  |          |   /`. '|  .---| \-.  \ ,`'--..._'--'  |  | 
        |  |   |  |,|   .|  .-'-'  |  '--.  .--'       |  |  \  ' |  |  |  |  \  '       .-')     //   |  | |  ||  | | .-')        |  /  | ||  | .-'-'  |  ||  |  \  '   __.  | 
        |  |.'.|  |_|       |\| |_.'  |  |  |          |  |   ' | |  |(_|  |   ' |      (OO  \   / \_) |  |\|  ||  |_|( OO )       |  |_.' (|  '--\| |_.'  ||  |   ' |  |   .'  
        |         | |  .-.  | |  .-.  |  |  |          |  |   / :,|  |_.|  |   / :       |   /  /\_  \ |  | |  ||  | | `-' /       |  .  '.'|  .--'|  .-.  ||  |   / :  |___|   
        |   ,'.   | |  | |  | |  | |  |  |  |          |  '--'  (_|  |  |  '--'  /       `-./  /.__)  `'  '-'  ('  '-'(_.-'        |  |\  \ |  `---|  | |  ||  '--'  /  .---.   
        '--'   '--' `--' `--' `--' `--'  `--'          `-------'  `--'  `-------'          `--'         `-----'  `-----'           `--' '--'`------`--' `--'`-------'   '---'  
        ''')
        @click.command()
        @click.option('--title', prompt='Enter Title: ')
        @click.option('--author', prompt='Enter Author: ')
        @click.option('--publish_date', prompt='Enter Publish_Date (MMDDYYYY format): ')
        @click.option('--read', prompt='Have you read this book? (Yes or No?): ')

        def add_book(title, author, publish_date, read):
            new_book = Books(
                title = title,
                author = author,
                publish_date = publish_date,
                read = read
                )

            session.add(new_book)
            session.commit()

        if __name__ == '__main__':
            add_book.main(standalone_mode=False)
        else:
            print('Read more books!')

    elif options == 3:
        print('''
                    ('-.  ('-.         (`-.     ('-.           ('-.           _  .-')    ('-.       (`-.            ('-.   (`\ .-') /,---. 
                  _(  OO)( OO ).-.   _(OO  )_ _(  OO)         ( OO ).-.      ( \( -O ) _(  OO)    _(OO  )_        _(  OO)   `.( OO ),|   | 
         ,--.    (,------/ . --. ,--(_/   ,. (,------.        / . --. /       ,------.(,------,--(_/   ,. \,-.-')(,------,--./  .--. |   | 
         |  |.-') |  .---| \-.  \\   \   /(__/|  .---'        | \-.  \        |   /`. '|  .---\   \   /(__/|  |OO)|  .---|      |  | |   | 
         |  | OO )|  | .-'-'  |  |\   \ /   / |  |          .-'-'  |  |       |  /  | ||  |    \   \ /   / |  |  \|  |   |  |   |  |,|   | 
         |  |`-' (|  '--\| |_.'  | \   '   /,(|  '--.        \| |_.'  |       |  |_.' (|  '--.  \   '   /, |  |(_(|  '--.|  |.'.|  |_|  .' 
        (|  '---.'|  .--'|  .-.  |  \     /__)|  .--'         |  .-.  |       |  .  '.'|  .--'   \     /__,|  |_.'|  .--'|         | `--'  
         |      | |  `---|  | |  |   \   /    |  `---.        |  | |  |       |  |\  \ |  `---.   \   /  (_|  |   |  `---|   ,'.   | .--.  
         `------' `------`--' `--'    `-'     `------'        `--' `--'       `--' '--'`------'    `-'     `--'   `------'--'   '--' '--'  
        ''')
        @click.command()
        @click.option('--review', prompt='Write your review! ')
        @click.option('--rating', prompt='What do you rate this book out of 5? ')
        @click.option('--book_id')
        @click.option('--user_id')

        def write_review(review, rating, book_id, user_id):
            new_review = Reviews(
                review = review,
                rating = rating,
                book_id = book_id,
                user_id = user_id
            )

            session.add(new_review)
            session.commit()

        if __name__ == '__main__':
            write_review.main(standalone_mode=False)
        else:
            print('Please leave a review next time!')

    else:
        print('''
               .-')                       .-') _   .-') _             .-') _                    _ (`-. _  .-')                        _  .-')    ('-.    _   .-')    
            .(  OO)                     (  OO) ) (  OO) )           ( OO ) )                  ( (OO  ( \( -O )                      ( \( -O )  ( OO ).-( '.( OO )_  
            (_)---\_)  ,--. ,--.   ,-.-')/     '._/     '._,-.-'),--./ ,--,' ,----.           _.`     \,------. .-'),-----.  ,----.   ,------.  / . --. /,--.   ,--.)
            '  .-.  '  |  | |  |   |  |OO|'--...__|'--...__|  |OO|   \ |  |\'  .-./-')       (__...--''|   /`. ( OO'  .-.  ''  .-./-')|   /`. ' | \-.  \ |   `.'   | 
           ,|  | |  |  |  | | .-') |  |  '--.  .--'--.  .--|  |  |    \|  | |  |_( O- )       |  /  | ||  /  | /   |  | |  ||  |_( O- |  /  | .-'-'  |  ||         | 
          (_|  | |  |  |  |_|( OO )|  |(_/  |  |     |  |  |  |(_|  .     |/|  | .--, \       |  |_.' ||  |_.' \_) |  |\|  ||  | .--, |  |_.' |\| |_.'  ||  |'.'|  | 
            |  | |  |  |  | | `-' ,|  |_.'  |  |     |  | ,|  |_.|  |\    |(|  | '. (_/       |  .___.'|  .  '.' \ |  | |  (|  | '. (_|  .  '.' |  .-.  ||  |   |  | 
            '  '-'  '-('  '-'(_.-(_|  |     |  |     |  |(_|  |  |  | \   | |  '--'  |        |  |     |  |\  \   `'  '-'  '|  '--'  ||  |\  \  |  | |  ||  |   |  | 
              `-----'--' `-----'    `--'     `--'     `--'  `--'  `--'  `--'  `------'         `--'     `--' '--'    `-----'  `------' `--' '--' `--' `--'`--'   `--' 
        ''')