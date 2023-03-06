
class Client:

    clients = 0

    def __init__(self, __id, name="None", cnp=-1):
        self.__id = __id
        nameArr = name.split()
        if len(nameArr) == 0:
            first = ""
        else:
            first = nameArr[0]
        if len(nameArr) < 1:
            last = ""
        else:
            last = nameArr[1:]
        self.__name = {"first": first,
                       "last": ' '.join(last)}
        self.__cnp = cnp
        self.__books = []
        self.clients += 1

    def getId(self):
        return self.__id

    def setId(self, __id):
        self.__id = __id

    def getName(self):
        name = self.__name["first"] + " " + self.__name["last"]
        return name

    def setName(self, name):
        nameArr = name.split()
        first, last = "", ""
        if len(nameArr) > 0:
            first = nameArr[0]
        if len(nameArr) > 1:
            last = nameArr[1]
        self.__name["first"] = first
        self.__name["last"] = last

    def getCnp(self):
        return self.__cnp

    def setCnp(self, cnp):
        self.__cnp = cnp

    def lendBook(self, book):
        self.__books.append(book)

    def returnBook(self, book):
        for b in self.__books:
            if b == book:
                self.__books.pop(self.__books.index(b))

    def getLentBooks(self):
        return self.__books

    def __str__(self):
        return f'{self.__id},{self.__name["first"] + " " + self.__name["last"]},{self.__cnp}'

    def __eq__(self, other):
        return self.__id == other.getId()
