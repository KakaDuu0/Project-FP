import re


class Validator:

    def __init__(self):
        pass

    def validateBook(self, book):
        if book.getTitle() == "":
            raise ValueError
        if len(book.getDescription()) < 10:
            raise ValueError
        if len(book.getAuthor()) < 2:
            raise ValueError

    def validateClient(self, client):
        if len(client.getName()) < 4:
            raise ValueError
        #if re.search(r'[0-6][0-9][0-9][0-1][0-2][0-3][0-9][0-4][0-9]+', str(client.getCnp())) is not None:
        #if re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', str(client.getCnp())) is not None:
           # raise ValueError
