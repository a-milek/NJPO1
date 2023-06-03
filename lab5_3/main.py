# Napisz program tworzący bazę danych z interfejsem konsolowym.
# Wymagane są następujące operacje,
# dodanie wiersza,
# usunięcie wiersza,
# zmiana pola wiersza,
# wyświetlenie opcji.
# Menu można zorganizować jako odczytywanie parametrów zwróconych
# przez funkcję `input` lub z pomocą komend (łatwiejszy sposób).

# Example table of Books:
# | id | title | author | ISBN |

import argparse
from contextlib import contextmanager
from platform import system
from tempfile import mktemp

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database

temp_db = mktemp(suffix='.sqlite')

print(f'Using {temp_db}')

conn_uri_handler = {
    'Windows': f'sqlite:///{temp_db}',
    'Darwin': f'sqlite:////{temp_db}',
    'Linux': f'sqlite:////{temp_db}',
    'Java': f'sqlite:////{temp_db}'
}

engine = create_engine(conn_uri_handler[system()])

Base = declarative_base(bind=engine)


# Table definition
class Book(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(128))
    author = Column('author', String(128))
    isbn = Column('isbn', String(128))


Base.metadata.create_all()

Session = sessionmaker(bind=engine)


@contextmanager
def create_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def provide_session(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        try:
            with create_session() as session:
                args = (*args, session) if args else (session,)
                return func(*args, **kwargs)
        except Exception as e:
            print(f'Error found: {e}')

        return None

    return wrapper


# Database operations
@provide_session
def populate(session):
    session.add(Book(id=1, title='Pan Lodowego Ogrodu', author='Jarosław Grzędowicz', isbn=9788374801620))
    session.add(Book(id=2, title='Wiedźmin: Ostatnie Życzenie', author='Andrzej Sapkowski', isbn=9788375780645))
    session.add(Book(id=3, title='Oko Jelenia. Droga do Nidaros', author='Andrzej Pilipiuk', isbn=9788375742605))


# add book (row)
@provide_session
def add_book(title, author, isbn, session):
    session.add(Book(title=title, author=author, isbn=isbn))


# delete book (row)
@provide_session
def delete_book(id, session):
    if session.query(Book).filter(Book.id == id).first() is not None:
        book = session.query(Book).filter(Book.id == id).first()
        session.delete(book)
    else:
        print('No such book')


# update book (row)
@provide_session
def update_book(id, column_to_update, new_value, session):
    book = session.query(Book).filter(Book.id == id).first()
    setattr(book, column_to_update, new_value)


@provide_session
def show_books(session):
    for book in session.query(Book).all():
        print('ID:', book.id, 'Title:', book.title, 'Author:', book.author, 'ISBN:', book.isbn)


@provide_session
def count_rows(session):
    return session.query(Book).count()


def exit_program():
    exit_program()


# Parser
# Show options can be achieved by -h or --help, so I didn't implement it separately
parser = argparse.ArgumentParser(description='Book database')
parser.add_argument('-a', '--add', nargs=3, metavar=('title', 'author', 'isbn'), help='Add book by providing '
                                                                                      'title, author and ISBN')
parser.add_argument('-d', '--delete', nargs=1, metavar='id', help='Delete book by id')
parser.add_argument('-u', '--update', nargs=3, metavar=('id', 'column', 'new_value'), help='Update book by id, provide '
                                                                                           'column name and new value')
parser.add_argument('-t', '--test', action='store_true', help='Run tests')
parser.add_argument('-e', '--exit_program', action='store_true', help='Exit')


# Tests
def test_add_book():
    rows_before = count_rows()
    add_book('Lód', 'Jacek Dukaj', 9788370540543)
    assert count_rows() == rows_before + 1


def test_delete_book():
    rows_before = count_rows()
    show_books()
    delete_book(1)
    show_books()
    assert count_rows() == rows_before - 1


@provide_session
def test_update_book(session):
    update_book(2, 'title', 'Wiedźmin: Pani Jeziora')
    assert session.query(Book).filter(Book.id == 2).first().title == 'Wiedźmin: Pani Jeziora'


def run_tests():
    test_add_book()
    test_delete_book()
    test_update_book()


if __name__ == "__main__":
    args = parser.parse_args()
    populate()

    if args.add:
        add_book(*args.add)
    elif args.delete:
        delete_book(*args.delete)
    elif args.update:
        update_book(*args.update)
    elif args.exit_program:
        exit_program()
    elif args.test:
        run_tests()
    else:
        exit(0)
