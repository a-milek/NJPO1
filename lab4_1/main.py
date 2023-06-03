# Zadanie 1
#
# Napisz dekorator, który autoryzuje użytkownika na podstawie podanego loginu i hasła.
# Do przechowywania danych należy wykorzystać klasę `shelve`. Do maskowania hasła można użyć następującej funkcji [...]
# Należy pamiętać, że `salt` należy utworzyć raz i zachować w chronionym pliku.

import binascii
import hashlib
import shelve
from os import urandom


def generate_salt():
    salt = hashlib.sha256(urandom(60)).hexdigest().encode('ascii')
    save_salt(salt)
    return salt


def save_salt(salt):
    with open('salt.txt', 'wb') as file:  # wb - write binary
        file.write(salt)


def get_salt():
    with open('salt.txt', 'rb') as file:  # rb - read binary
        return file.read()


def read_salt():
    return get_salt()


def hash_password(password):
    """Hash a password for storing."""
    salt = read_salt()
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def add_user(login, password):
    with shelve.open('users') as users:
        users[login] = hash_password(password)


def remove_user(login):
    with shelve.open('users') as users:
        if login in users:
            del users[login]


def remove_all_users():
    with shelve.open('users') as users:
        users.clear()


# For testing purposes
def setup():
    generate_salt()
    add_user(return_default_login(), return_default_password())


def teardown():
    remove_all_users()


def return_default_login():
    return 'default_login'


def return_default_password():
    return 'default_password'


def authenticate(login, password):
    with shelve.open('users') as users:
        if login in users:
            retrieved_password = users[login]
            password_hash = hash_password(password)
            if password_hash == retrieved_password:
                return True
        else:
            return False


def authorized(thing_to_authorize):
    # For testing purposes
    login = return_default_login()
    password = return_default_password()

    def inner():
        if authenticate(login, password):
            return thing_to_authorize()
        else:
            print('You are not authorized to execute this function')
            return False

    return inner


@authorized
def authorized_only_function():
    print('Authorized only function has been executed')
    return True


if __name__ == '__main__':
    setup()
    assert authorized_only_function() is True
    teardown()
    assert authorized_only_function() is False
