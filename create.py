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
while options != 6:
    print('(1) Let me steal your data!')
    print('(2) Want to add a book?')
    print('(3) Write a review?')
    print('(4) Wanna see who read the most books?')
    print('(5) Wanna see which book has the most reviews?')
    print('(6) QUIT now before I steal your data!!!')

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
            click.echo('User Data Stolen!')

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
        @click.option('--read', prompt='Have you read this book? (Yes or No?): ')

        def add_book(title, author, read):
            new_book = Books(
                title = title,
                author = author,
                read = read
                )

            session.add(new_book)
            session.commit()
            click.echo('Book Stolen!')

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

        books = session.query(Books).all()
        book_info = dict()
        for book in books:
            book_info[book.id] = book
        print(books)

        while True:
            try:
                book_id = int(input('search a book ID: '))
            except ValueError:
                print('input must be an integer')
                continue
            if not book_id in list(book_info.keys()):
                print('book ID does not exist')
            else:
                break
        
        users = session.query(User).all()
        user_info = dict()
        for user in users:
            user_info[user.id] = user
        print(users)

        while True:
            try:
                user_id = int(input("search a user ID: "))
            except ValueError:
                print('input must be an integer')
                continue
            if not user_id in list(user_info.keys()):
                print('user ID does not exist')
            else:
                break

        @click.command()
        @click.option('--review', prompt='Write your review! ')
        @click.option('--rating', prompt='What do you rate this book out of 5? ')

        def write_review(review, rating, book_id=book_id, user_id=user_id):
            new_review = Reviews(
                review = review,
                rating = rating,
                book_id = book_id,
                user_id = user_id
            )

            session.add(new_review)
            session.commit()
            click.echo('Review Stolen!')

        if __name__ == '__main__':
            write_review.main(standalone_mode=False)
        else:
            print('Please leave a review next time!')
        
    elif options == 4:
        print('''
        .-. .-')   ('-.   .-')   .-') _          _  .-')    ('-.  ('-.    _ .-') _    ('-. _  .-') ,---. 
        \  ( OO )_(  OO) ( OO ).(  OO) )        ( \( -O ) _(  OO)( OO ).-( (  OO) ) _(  OO( \( -O )|   | 
         ;-----.(,------(_)---\_/     '._        ,------.(,------/ . --. /\     .'_(,------,------.|   | 
         | .-.  ||  .---/    _ ||'--...__)       |   /`. '|  .---| \-.  \ ,`'--..._)|  .---|   /`. |   | 
         | '-' /_|  |   \  :` `.'--.  .--'       |  /  | ||  | .-'-'  |  ||  |  \  '|  |   |  /  | |   | 
         | .-. `(|  '--. '..`''.)  |  |          |  |_.' (|  '--\| |_.'  ||  |   ' (|  '--.|  |_.' |  .' 
         | |  \  |  .--'.-._)   \  |  |          |  .  '.'|  .--'|  .-.  ||  |   / :|  .--'|  .  '.`--'  
         | '--'  |  `---\       /  |  |          |  |\  \ |  `---|  | |  ||  '--'  /|  `---|  |\  \.--.  
         `------'`------'`-----'   `--'          `--' '--'`------`--' `--'`-------' `------`--' '--'--'  
        ''')

        print()

    elif options == 5:
        print('''
        .-. .-')   ('-.   .-')   .-') _         .-. .-')                         .-. .-') ,---. 
        \  ( OO )_(  OO) ( OO ).(  OO) )        \  ( OO )                        \  ( OO )|   | 
         ;-----.(,------(_)---\_/     '._        ;-----.\ .-'),-----. .-'),-----.,--. ,--.|   | 
         | .-.  ||  .---/    _ ||'--...__)       | .-.  |( OO'  .-.  ( OO'  .-.  |  .'   /|   | 
         | '-' /_|  |   \  :` `.'--.  .--'       | '-' /_/   |  | |  /   |  | |  |      /,|   | 
         | .-. `(|  '--. '..`''.)  |  |          | .-. `.\_) |  |\|  \_) |  |\|  |     ' _|  .' 
         | |  \  |  .--'.-._)   \  |  |          | |  \  | \ |  | |  | \ |  | |  |  .   \ `--'  
         | '--'  |  `---\       /  |  |          | '--'  /  `'  '-'  '  `'  '-'  |  |\   \.--.  
         `------'`------'`-----'   `--'          `------'     `-----'     `-----'`--' '--''--'  
        ''')

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