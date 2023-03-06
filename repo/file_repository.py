from repo.repository import Repository
from model.Client import Client
from model.Book import Book
from os import path


def getFilePath(filename):
    cur_path = path.dirname(__file__)
    return cur_path + f'\\..\\storage\\{filename}'


class FileRepository(Repository):

    def __init__(self, filename_c, filename_b):
        Repository.__init__(self)
        self.__filepath_c = getFilePath(filename_c)
        self.__filepath_b = getFilePath(filename_b)
        # self.__clearFileContents()
        self.__loadFromFile()

    def __clearFileContents(self):
        """
        Sterge toate datele din fisier
        :return: -
        """
        try:
            f = open(self.__filepath_c, "w")
            f.close()
        except IOError:
            pass

        try:
            f = open(self.__filepath_b, "w")
            f.close()
        except IOError:
            pass

        return

    def __loadFromFile(self):
        """
        Incarca datele clientilor din fisier in repo daca exista fisierul, altfel o creaza
        :return: -
        """
        try:
            with open(self.__filepath_c, "r") as file:
                line = file.readline().strip()
                while line != "":
                    line = line.split(",")
                    client = Client(int(line[0]), line[1], int(line[2]))
                    # the appended clients id might be different from the one that was read from file
                    Repository.addClient(self, client)
                    line = file.readline().strip()
        except FileNotFoundError:
            f = open(self.__filepath_c, "x")
            f.close()

        try:
            with open(self.__filepath_b, "r") as file:
                line = file.readline().strip()
                while line != "":
                    line = line.split(",")
                    book = Book(int(line[0]), line[1], line[3], line[2])
                    # the appended clients id might be different from the one that was read from file
                    Repository.addBook(self, book)
                    line = file.readline().strip()
        except FileNotFoundError:
            f = open(self.__filepath_b, "x")
            f.close()

    def __saveToFile(self):
        """
        Incarca datele clientilor din repo in fisier
        :return: -
        """
        with open(self.__filepath_c, "w") as file:
            clients = self.getAllClients()
            for client in clients:
                s = str(client) + "\n"
                file.write(s)

        with open(self.__filepath_b, "w") as file:
            books = self.getAllBooks()
            for book in books:
                s = str(book) + '\n'
                file.write(s)

    def addClient(self, client):
        Repository.addClient(self, client)
        self.__saveToFile()

    def editClient(self, client_to_edit):
        Repository.editClient(self, client_to_edit)
        self.__saveToFile()

    def removeClient(self, client_to_remove):
        Repository.removeClient(self, client_to_remove)
        self.__saveToFile()

    def addBook(self, book):
        Repository.addBook(self, book)
        self.__saveToFile()

    def removeBook(self, book_to_remove):
        Repository.removeBook(self, book_to_remove)
        self.__saveToFile()

    def editBook(self, book_to_edit):
        Repository.editBook(self, book_to_edit)
        self.__saveToFile()
