from collections import defaultdict


class Repository:

    def __init__(self):
        self.__clients = []
        self.__books = []

    def getAllClients(self):
        """
        Returneaza lista de clienti
        :return: list
        """
        return self.__clients

    def getAllBooks(self):
        """
        Returneaza lista de carti
        :return: list
        """
        return self.__books

    def addBook(self, book):
        book.setId(len(self.__books))
        self.__books.append(book)

    def addClient(self, client):
        """
        Adauga client in lista
        :param client: object
        :return: -
        """
        for c in self.__clients:
            if client.getCnp() == c.getCnp():
                raise ValueError
        client.setId(len(self.__clients))
        self.__clients.append(client)

    def removeBook(self, book_to_remove):
        """
        Stergere carte din lista
        :param book_to_remove: object
        :return: -
        """
        for book in self.__books:
            if book.getId() == book_to_remove.getId():
                self.__books.pop(self.__books.index(book))

    def removeClient(self, client_to_remove):
        """
        Stergere client din baza de date
        :param client_to_remove: object
        :return: -
        """
        for client in self.__clients:
            if client.getId() == client_to_remove.getId():
                self.__clients.pop(self.__clients.index(client))

    def editBook(self, book_to_edit):
        """
        Editare carte
        :param book_to_edit: object
        :return: -
        """
        for index in range(len(self.__books)):
            if self.__books[index].getId() == book_to_edit.getId():
                self.__books[index] = book_to_edit

    def editClient(self, client_to_edit):
        """
        Editare client
        :param client_to_edit: object
        :return: -
        """
        for index in range(len(self.__clients)):
            if self.__clients[index].getId() == client_to_edit.getId():
                self.__clients[index] = client_to_edit

    def getBook(self, book):
        """
        Cauta carte in baza de date si o returneaza
        :param book: object
        :return: list
        """
        books = []
        for index in range(len(self.__books)):
            if book.getTitle().lower() in self.__books[index].getTitle().lower():
                books.append(self.__books[index])
        return books if len(books) > 0 else None

    def getClient(self, client):
        """
        Cauta client in baza de date si il returneaza
        :param client: object
        :return: list
        """
        clients = []
        for index in range(len(self.__clients)):
            if client.getName().lower() in self.__clients[index].getName().lower():
                clients.append(self.__clients[index])
        return clients if len(clients) > 0 else None

    def addBookToClient(self, book, client):
        """
        Adauga carte la lista de carti inchiriate a unui client
        :param book: object
        :param client: object
        :return: -
        """
        lentBooks = client.getLentBooks()
        for lb in lentBooks:
            if lb.getId() == book.getId():
                return
        client.lendBook(book)

    def removeBookFromClient(self, book, client):
        """
        Sterge o carte din lista de carti inchiriate a unui client
        :param book: object
        :param client: object
        :return: -
        """
        lentBooks = client.getLentBooks()
        found = False
        for lb in lentBooks:
            if lb.getId() == book.getId():
                found = True
        if found:
            client.returnBook(book)

    def getMostLentBooks(self):
        """
        n = lungimea listei de carti
        m = lungimea listei de clienti
        p = numarul de carti inchiriate de client
        => O(n + m*p + nlogn) complexitate de timp
        => O(n + m) best case scenario
        => O(n + m*p + n^2) worst case scenario
        Returns primii 3 cele mai inchiriate carti
        :return: list
        """
        bookIndex = defaultdict(int)
        # n
        for i in range(len(self.__books)):
            bookIndex[i] = 0

        # m*p
        for client in self.__clients:
            for book in client.getLentBooks():
                bookIndex[book.getId()] += 1

        # nlogn
        bookIndex = sorted(bookIndex, key=bookIndex.get, reverse=True)
        return [self.__books[bookIndex[0]], self.__books[bookIndex[1]], self.__books[bookIndex[2]]]

    # def getSortedClients(self):
    #     """
    #     Returneaza o lista sortata dupa clientii cu cele mai multe carti inchiriate
    #     :return: list
    #     """
    #     clientIndex = defaultdict(int)
    #     for i in range(len(self.__clients)):
    #         clientIndex[i] = 0
    #
    #     for client in self.__clients:
    #         clientIndex[client.getId()] = len(client.getLentBooks())
    #
    #     clientIndex = sorted(clientIndex, key=clientIndex.get, reverse=True)
    #     sortedClients = []
    #     for i in clientIndex:
    #         sortedClients.append(self.__clients[i])
    #
    #     return sortedClients

    def getNextGap(self, gap):

        # Shrink gap by Shrink factor
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    def combSort(self, arr, key=lambda k: k, reversed=False, cmp=lambda x, y: x > y):
        n = len(arr)

        # Initialize gap
        gap = n

        # Initialize swapped as true to make sure that
        # loop runs
        swapped = True

        # Keep running while gap is more than 1 and last
        # iteration caused a swap
        while gap != 1 or swapped == 1:

            # Find next gap
            gap = self.getNextGap(gap)

            # Initialize swapped as false so that we can
            # check if swap happened or not
            swapped = False

            # Compare all elements with current gap
            for i in range(0, n - gap):
                if cmp(key(arr[i]), key(arr[i + gap])):
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True

        if reversed:
            arr.reverse()

        return arr

    def insertionSort(self, array, key=lambda k: k, reverse=False, cmp=lambda x, y: x > y):
        for step in range(1, len(array)):
            e = key(array[step])
            j = step - 1

            while j >= 0 and cmp(e, key(array[j])):
                array[j + 1] = array[j]
                j = j - 1

            array[j + 1] = e

        if reverse:
            array.reverse()
        return array

    def compareClient(self, c1, c2, k1=lambda k: len(k.getLentBooks()), k2=lambda k: k.getId()):
        if k1(c1) > k1(c2):
            return True
        elif k1(c1) < k1(c2):
            return False
        else:
            if k2(c1) >= k2(c2):
                return True
            else:
                return False
