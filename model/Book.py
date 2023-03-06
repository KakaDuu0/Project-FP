

class Book:

    books = 0

    def __init__(self, __id, title="None", description="NoneNoneNone", author="None"):
        self.__id = __id
        self.__title = title
        self.__description = description
        self.__author = author
        # self.__clients = []

    def getId(self):
        return self.__id

    def setId(self, __id):
        self.__id = __id

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def getAuthor(self):
        return self.__author

    def setAuthor(self, author):
        self.__author = author

    # def addClient(self, client):
    #    self.__clients.append(client)

    # def getClients(self):
    #     return self.__clients

    # def removeClient(self, client):
    #     for c in self.__clients:
    #         if c == client:
    #             self.__clients.pop(self.__clients.index(c))

    def __str__(self):
        return f'{self.__id},{self.__title},{self.__author},{self.__description}'

    def __eq__(self, other):
        return self.__id == other.getId()
