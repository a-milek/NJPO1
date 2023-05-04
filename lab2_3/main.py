# Zadanie 3
# Stwórz kolekcję książek zawierającą takie pola jak
# `tytuł`,`gatunek`,`autor`,`isbn`.
# Napisz trzy funkcje,
# (i) zapisującą kolekcję,
# (ii) odczytującą kolekcję,
# (iii) obliczająca statystykę wg. gatunku i autora.
import pickle
from collections import namedtuple


def save_collection(collection):
    with open("books.pkl", "wb") as file:
        pickle.dump(collection, file)


def import_collection(file_name):
    with open(file_name, 'rb') as file:
        collection = pickle.load(file)
    return collection


# not sure about the statistics, mixed signals(again) from the lecture and from the exercise itself
def statistics(value, collection):
    count = 0
    for book in collection:
        if value in book:
            count += 1
    return count


if __name__ == '__main__':
    Book = namedtuple('Book', ['title', 'genre', 'author', 'isbn'])

    save_collection([Book('Miecz Przeznaczenia', 'Fantasy', 'Sapkowski', 282),
                     Book('Hobbit', 'Fantasy', 'Tolkien', 619),
                     Book('Krew Elfow', 'Fantasy', 'Sapkowski', 231),
                     Book('Wieza Jaksolki', 'Fantasy', 'Sapkowski', 32),
                     Book('Brak Tchu', 'Novel', 'Orwell', 1232)
                     ])
    col = import_collection('books.pkl')
    print(statistics('Sapkowski', col))
