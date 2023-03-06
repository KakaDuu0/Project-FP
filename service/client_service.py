from model.Client import Client
from functions import generator
from math import floor


def getClientsString(clients):
    clientsString = []
    for client in clients:
        booksString = []
        for book in client.getLentBooks():
            booksString.append(f'#{book.getId()}: {book.getTitle()} - {book.getAuthor()}')
        clientsString.append(f'#{client.getId()}: {client.getName()} - {client.getCnp()}\n'
                             f'\tBooks: {", ".join(booksString) if len(booksString) > 0 else "None"}')
    return clientsString


class ClientService:

    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def add(self, client):
        """
        Adaugare client
        :param client: object
        :return: -
        """
        client = Client(-1, client.getName(), client.getCnp())
        self.__validator.validateClient(client)
        self.__repo.addClient(client)

    def edit(self, client):
        """
        Editare client
        :param client: object
        :return: -
        """
        client = Client(client.getId(), client.getName(), client.getCnp())
        self.__validator.validateClient(client)
        self.__repo.editClient(client)

    def remove(self, client):
        """
        Stergere client
        :param client: object
        :return: -
        """
        client = Client(client.getId())
        self.__validator.validateClient(client)
        self.__repo.removeClient(client)

    def search(self, client, return_type="str"):
        """
        Cautare client
        :param client: object
        :param return_type: string
        :return: string if return_type=="str" else list
        """
        client = Client(-1, name=client.getName())
        self.__validator.validateClient(client)
        clients = self.__repo.getClient(client)
        if return_type != 'str':
            return clients
        if clients is not None:
            clientsString = getClientsString(clients)
            return '\n'.join(clientsString)
        return "No clients found."

    def generate(self, num):
        """
        Genereaza num clienti dupa care le adauga in baza de date
        :param num: int
        :return: ultimul client generat
        """
        generated_clients = generator.generateClients(num)
        lastClient = None
        for client in generated_clients:
            self.add(client)
            lastClient = client

        return lastClient

    def addBook(self, client, book):
        """
        Adaugare carte in lista de carti inchiriate de client
        :param client: object
        :param book: object
        :return: -
        """
        self.__repo.addBookToClient(book, client)

    def removeBook(self, client, book):
        """
        Stergere carte din lista de carti inchiriate de client
        :param client: object
        :param book: object
        :return: -
        """
        self.__repo.removeBookFromClient(book, client)

    def getAllClients(self):
        """
        Returneaza toti clientii din baza de date formatata ca string
        :return: string
        """
        clients = self.__repo.getAllClients()
        clientsString = getClientsString(clients)
        return '\n'.join(clientsString) if len(clientsString) > 0 else 'No clients registered in database.'

    def getAverageBooks(self):
        """
        Numara media de carti inchiriate de un client si returneaza acest numar
        :return: float
        """
        clients = self.__repo.getAllClients()
        s = 0
        nr = 0
        for client in clients:
            s += len(client.getLentBooks())
            nr += 1
        if s == 0:
            return 0
        return s / nr

    def getSortedClients(self):
        """
        Returneaza un string sortat cu clientii cu cele mai multe carti inchiriate
        :return: string
        """
        return self.__sortClients(-1)

    def getMostActiveClients(self):
        """
        Returneaza un string cu primii 20% cei mai activi clienti
        :return: string
        """
        return self.__sortClients(1)

    def __sortClients(self, length):
        """
        Construieste un string dupa clinetii sortati dupa cele mai multe carti inchiriate
        :param length: int
        :return: string
        """
        clientsList = self.__repo.insertionSort(self.__repo.getAllClients(), cmp=self.__repo.compareClient)
        string = ''
        if length == -1:
            length = len(clientsList)
        else:
            length = floor(len(clientsList) * 0.2)
            if length < 1 and length != 0:
                length = 1
        for i in range(length):
            string += f'#{i + 1}: {clientsList[i].getName()} - {len(clientsList[i].getLentBooks())}\n'
        return string
