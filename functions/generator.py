from model.Client import Client
from model.Book import Book
import random
import string


def generateClients(num):
    """
    Genereaza o lista de clienti cu date aleoatorii
    :param num: int
    :return: list
    """
    clients = []
    letters = string.ascii_letters
    for i in range(num):
        name = ''.join(random.choice(letters) for _ in range(12))\
               + " " + ''.join(random.choice(letters) for _ in range(9))
        cnp = generateCnp()
        client = Client(-1, name, cnp)
        clients.append(client)
    return clients


def generateClientsRecursive(num, clients):
    if num > 0:
        letters = string.ascii_letters
        name = ''.join(random.choice(letters) for _ in range(12)) \
               + " " + ''.join(random.choice(letters) for _ in range(9))
        cnp = generateCnp()
        client = Client(-1, name, cnp)
        clients.append(client)
        generateClientsRecursive(num - 1, clients)
    else:
        return clients

def generateCnp():
    """
    Genereaza CNP valid (aproape)
    :return: int
    """
    generation_digit = round(random.random() * 5) * (10 ** 12)
    year_digit = round(random.random()*99) * (10 ** 10)
    month_digit = round(random.random()*12) * (10 ** 8)
    day_digit = round(random.random()*31) * (10 ** 6)
    county_digit = round(random.random()*41) * (10 ** 4)
    other_digits = round(random.random() * (10 ** 3))
    return generation_digit + year_digit + month_digit + day_digit + county_digit + other_digits


def generateBooks(num):
    """
    Genereaza o lista de caarti cu date aleatorii
    :param num: int
    :return: list
    """
    books = []
    letters = string.ascii_letters
    for i in range(num):
        title = ''.join(random.choice(letters) for _ in range(round(random.random() * 10 + 2)))
        description = ''.join(random.choice(letters) for _ in range(round(random.random() * 30 + 10)))
        author = ''.join(random.choice(letters) for _ in range(round(random.random() * 10 + 2)))
        book = Book(-1, title=title, description=description, author=author)
        books.append(book)
    return books


def generateBooksRecursive(num, books):
    if num > 0:
        letters = string.ascii_letters
        title = ''.join(random.choice(letters) for _ in range(round(random.random() * 10 + 2)))
        description = ''.join(random.choice(letters) for _ in range(round(random.random() * 30 + 10)))
        author = ''.join(random.choice(letters) for _ in range(round(random.random() * 10 + 2)))
        book = Book(-1, title=title, description=description, author=author)
        books.append(book)
        generateBooksRecursive(num - 1, books)
    else:
        return books
