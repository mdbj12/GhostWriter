from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from models import Base, User, Books, Reviews
import click
import time

print(f'''
                 ('-. .-.               .-')    .-') _           (`\ .-') /` _  .-')           .-') _     ('-.  _  .-')   
                ( OO )  /              ( OO ). (  OO) )           `.( OO ),'( \( -O )         (  OO) )  _(  OO)( \( -O )  
     ,----.    ,--. ,--. .-'),-----. (_)---\_)/     '._       ,--./  .--.   ,------.  ,-.-') /     '._(,------.,------.  
    '  .-./-') |  | |  |( OO'  .-.  '/    _ | |'--...__)      |      |  |   |   /`. ' |  |OO)|'--...__)|  .---'|   /`. ' 
    |  |_( O- )|   .|  |/   |  | |  |\  :` `. '--.  .--'      |  |   |  |,  |  /  | | |  |  \'--.  .--'|  |    |  /  | | 
    |  | .--, \|       |\_) |  |\|  | '..`''.)   |  |         |  |.'.|  |_) |  |_.' | |  |(_/   |  |  (|  '--. |  |_.' | 
   (|  | '. (_/|  .-.  |  \ |  | |  |.-._)   \   |  |         |         |   |  .  '.',|  |_.'   |  |   |  .--' |  .  '.' 
    |  '--'  | |  | |  |   `'  '-'  '\       /   |  |         |   ,'.   |   |  |\  \(_|  |      |  |   |  `---.|  |\  \  
     `------'  `--' `--'     `-----'  `-----'    `--'         '--'   '--'   `--' '--' `--'      `--'   `------'`--' '--' 
''')
      
time.sleep(1)

print(f'''
loading books....
generating user....
loading reviews....
compiling data....
''')
      
time.sleep(1)

engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user_options = 0
while user_options != 3:
    click.echo('(1) Create new UserID!')
    click.echo('(2) Select existing UserID!')
    click.echo('(3) Quit Program!')

    user_options = int(input())

    if user_options == 1:

        time.sleep(1)

        click.echo('''
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

        time.sleep(1)

        @click.command()
        @click.option('--name', prompt='Enter name: ')
        @click.option('--age', type=int, prompt='Enter age: ')
        @click.option('--fav_genre', prompt='Enter favorite genre: ')

        def create_user(name,age,fav_genre):
            new_user = User(
                name = name,
                age = age,
                fav_genre = fav_genre
                )
            session.add(new_user)
            session.commit()

            time.sleep(1)
            click.echo('')
            click.echo('===============================================')
            click.echo(f'=====   Welcome to Ghost Writer {new_user.name}!   =====')
            click.echo('===============================================')
            click.echo('')

        if __name__ == '__main__':
            create_user.main(standalone_mode=False)
    
    elif user_options == 2:
        users = session.query(User).all()
        user_info = dict()
        for user in users:
            user_info[user.id] = user
        click.echo(users)

        while True:
            try:
                user_id = int(input('Which UserID are you? '))
            except ValueError:
                click.echo('Input must be an Integer')
                continue
            if user_id not in list(user_info.keys()):
                click.echo('UserID does not exist!')
            else:
                user_id = user.name
                break

        def current_user(name, age, fav_genre):
            user_instance = User(
                name = name,
                age = age,
                fav_genre = fav_genre
            )

            session.add(user_instance)
            session.commit()

        menu_options = 0
        while menu_options != 4:
            click.echo('(1) Want to add a book?')
            click.echo('(2) Write a review?')
            click.echo('(3) See Book Reviews?')
            click.echo('(4) Back to UserID')

            menu_options = int(input())

            if menu_options == 1:
                click.echo('''
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

                time.sleep(1)

                @click.command()
                @click.option('--title', prompt='Enter Title: ')
                @click.option('--author', prompt='Enter Author: ')
                @click.option('--read', type=bool, prompt='Have you read this book? (True or False?): ')

                def add_book(title, author, read):
                    new_book = Books(
                        title = title,
                        author = author,
                        read = read
                        )

                    session.add(new_book)
                    session.commit()

                    click.echo('')
                    click.echo('====================')
                    click.echo('=== Book Stolen! ===')
                    click.echo('====================')
                    click.echo('')

                if __name__ == '__main__':
                    add_book.main(standalone_mode=False)
                continue

            elif menu_options == 2:
                click.echo('''
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

                click.echo('')
                click.echo('===========================')
                click.echo('===== Loading Data... =====')
                click.echo('===========================')
                time.sleep(2)

                users = session.query(User).all()
                user_info = dict()
                for user in users:
                    user_info[user.id] = user

                click.echo('')
                click.echo('===========================')
                click.echo('===== Loading Data... =====')
                click.echo('===========================')
                time.sleep(2)
                click.echo(users)
                time.sleep(1)

                while True:
                    try:
                        user_id = int(input("search a user ID: "))
                    except ValueError:
                        click.echo('input must be an integer')
                        continue
                    if user_id not in list(user_info.keys()):
                        click.echo('user ID does not exist')
                    else:
                        break
                
                time.sleep(1)
                search_options = 0
                while search_options != 3:
                    click.echo('(1) Search by Book ID? ')
                    click.echo('(2) Search by Book Title/Author? ')
                    click.echo('(3) Reviews done')
                    search_options = int(input())

                    if search_options == 1:

                        click.echo('')
                        click.echo('============================')
                        click.echo('===== Loading Books... =====')
                        click.echo('============================')
                        click.echo('')

                        books = session.query(Books).all()
                        book_info = dict()
                        for book in books:
                            book_info[book.id] = book

                        click.echo('')
                        click.echo('===========================')
                        click.echo('===== Loading Data... =====')
                        click.echo('===========================')
                        click.echo('')
                        time.sleep(2)
                        click.echo(books)
                        time.sleep(1)

                        while True:
                            try:
                                time.sleep(1)
                                book_id = int(input('Search a book ID: '))
                            except ValueError:
                                click.echo('Input must be an Integer')
                                continue
                            if not book_id in list(book_info.keys()):
                                click.echo('Book ID does not exist')
                            else:
                                book = books[book_id - 1]
                                book_title = book.title
                                book_author = book.author
                                break

                        time.sleep(1)
                        @click.command()
                        @click.option('--review', prompt='Write your review! ')
                        @click.option('--rating', type=click.IntRange(1, 5), prompt='What do you rate this book out of 5? ')

                        def write_review(review, rating, book_id=book_id, user_id=user_id, book_title=book.title, book_author=book.author):
                            new_review = Reviews(
                                user_id = user_id,
                                book_id = book_id,
                                book_title = book_title,
                                book_author = book_author,
                                review = review,
                                rating = rating
                            )

                            session.add(new_review)
                            session.commit()

                            time.sleep(1)
                            click.echo('')
                            click.echo('==========================')
                            click.echo('===== Review Stolen! =====')
                            click.echo('==========================')
                            click.echo('')
                    
                        if __name__ == '__main__':
                            write_review.main(standalone_mode=False)

                    elif search_options == 2:

                        books = session.query(Books).all()
                        book_titles = dict()
                        for title in books:
                            book_titles[title.title] = title

                        click.echo('')
                        click.echo('============================')
                        click.echo('===== Loading Books... =====')
                        click.echo('============================')
                        time.sleep(2)
                        click.echo(books)
                        time.sleep(1)

                        while True:
                            try:
                                time.sleep(1)
                                book_title = str(input('Search a Book Title: '))
                            except ValueError:
                                click.echo('input must be an existing book')
                                continue
                            if book_title not in list(book_titles.keys()):
                                click.echo('Book title does not exist')
                            else:
                                book_id = title.id
                                break

                        authors = session.query(Books).all()
                        book_authors = dict()
                        for author in authors:
                            book_authors[author.author] = author

                        click.echo('')
                        click.echo('==============================')
                        click.echo('===== Loading Authors... =====')
                        click.echo('==============================')
                        time.sleep(2)
                        click.echo(authors)
                        time.sleep(1)

                        while True:
                            try:
                                time.sleep(1)
                                book_author = str(input('Search a Book Author: '))
                            except ValueError:
                                click.echo('input must be an existing author')
                                continue
                            if book_author not in list(book_authors.keys()):
                                click.echo('Book Author does not exist')
                            else:
                                book_author = author.author
                                break

                        @click.command()
                        @click.option('--review', prompt='Write your review! ')
                        @click.option('--rating', type=click.IntRange(1, 5), prompt='What do you rate this book out of 5? ')

                        def write_review(review, rating, book_id=book_id, user_id=user_id, book_title=book_title, book_author=book_author):
                            new_review = Reviews(
                                user_id = user_id,
                                book_id = book_id,
                                book_title = book_title,
                                book_author = book_author,
                                review = review,
                                rating = rating,
                            )

                            session.add(new_review)
                            session.commit()
                            time.sleep(1)
                        click.echo('')
                        click.echo('==================================')
                        click.echo('========  EXITING REVIEWS ========')
                        click.echo('==================================')
                        click.echo('')
                    
                        if __name__ == '__main__':
                            write_review.main(standalone_mode=False)
                    else:
                        time.sleep(1)
                        click.echo('')
                        click.echo('==================================')
                        click.echo('========  EXITING REVIEWS ========')
                        click.echo('==================================')
                        click.echo('')

            elif menu_options == 3:


                review_options = 0
                while review_options != 3:
                    click.echo('Find your favorite book and see its reviews!')
                    click.echo('(1) Search by BookID: ')
                    click.echo('(2) Search by Book Title/Author: ')

                    review_options = int(input())

                    if review_options == 1:
                        click.echo('')
                        click.echo('============================')
                        click.echo('===== Loading Books... =====')
                        click.echo('============================')
                        click.echo('')

                        books = session.query(Books).all()
                        book_info = dict()
                        for book in books:
                            book_info[book.id] = book

                        click.echo('')
                        click.echo('===========================')
                        click.echo('===== Loading Data... =====')
                        click.echo('===========================')
                        click.echo('')
                        time.sleep(2)
                        click.echo(books)
                        time.sleep(1)

                        while True:
                            try:
                                time.sleep(1)
                                book_id = int(input('Search a book ID: '))
                            except ValueError:
                                click.echo('Input must be an Integer')
                                continue
                            if not book_id in list(book_info.keys()):
                                click.echo('Book ID does not exist')
                            else:
                                book = books[book_id - 1]
                                book_title = book.title
                                book_author = book.author
                                break

                        reviews = session.query(Reviews).filter_by(book_id = book_id).all()
                        book = session.query(Books).filter_by(id = book_id).first()
                        
                        click.echo(f'Book Found! All reviews1 for {book_title} by {book_author}: \n {reviews}')
                    
                        session.commit()

                    elif review_options == 2:
                        books = session.query(Books).all()
                        book_titles = dict()
                        for title in books:
                            book_titles[title.title] = title

                        click.echo('')
                        click.echo('============================')
                        click.echo('===== Loading Books... =====')
                        click.echo('============================')
                        time.sleep(2)
                        click.echo(books)
                        time.sleep(1)

                        while True:
                            try:
                                time.sleep(1)
                                book_title = str(input('Search a Book Title: '))
                            except ValueError:
                                click.echo('input must be an existing book')
                                continue
                            if book_title not in list(book_titles.keys()):
                                click.echo('Book title does not exist')
                            else:
                                book_id = title.id
                                break

                        authors = session.query(Books).all()
                        book_authors = dict()
                        for author in authors:
                            book_authors[author.author] = author

                        click.echo('')
                        click.echo('==============================')
                        click.echo('===== Loading Authors... =====')
                        click.echo('==============================')
                        time.sleep(2)
                        click.echo(authors)
                        time.sleep(1)

                        while True:
                            try:
                                time.sleep(1)
                                book_author = str(input('Search a Book Author: '))
                            except ValueError:
                                click.echo('input must be an existing author')
                                continue
                            if book_author not in list((book_authors.keys())):
                                click.echo('Book Author does not exist')
                            else:
                                author = book_authors[book_author]
                                book_author = book_authors[author]
                                break
                        
                        reviews = session.query(Reviews).filter_by(book_title = book_title).filter_by(book_author = book_author).all()
                        
                        click.echo(f'Book Found! All reviews for {book_title} by {book_author}: \n {reviews}')

                    elif review_options == 3:
                        click.echo('============================')
                        click.echo('======== LOADING... ========')
                        click.echo('============================')

                time.sleep(1)

            elif menu_options == 4:

                time.sleep(1)

                click.echo('''
                                          ('-.     _ .-') _                .-') _             
                                         ( OO ).-.( (  OO) )              ( OO ) )            
                 ,--.      .-'),-----.   / . --. / \     .'_   ,-.-') ,--./ ,--,'  ,----.     
                 |  |.-') ( OO'  .-.  '  | \-.  \  ,`'--..._)  |  |OO)|   \ |  |\ '  .-./-')  
                 |  | OO )/   |  | |  |.-'-'  |  | |  |  \  '  |  |  \|    \|  | )|  |_( O- ) 
                 |  |`-' |\_) |  |\|  | \| |_.'  | |  |   ' |  |  |(_/|  .     |/ |  | .--, \ 
                (|  '---.'  \ |  | |  |  |  .-.  | |  |   / : ,|  |_.'|  |\    | (|  | '. (_/ 
                 |      |    `'  '-'  '  |  | |  | |  '--'  /(_|  |   |  | \   |  |  '--'  |  .-..-..-. 
                 `------'      `-----'   `--' `--' `-------'   `--'   `--'  `--'   `------'   `-'`-'`-' 
                ''')

                time.sleep(2)

    else:
            time.sleep(1)
            click.echo('''
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