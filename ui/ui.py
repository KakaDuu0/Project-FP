import time

from model.Book import Book
from model.Client import Client


def printOptions():
    """
        Construieste un string formatat cu optiunile valabile pentru utilizator si returneaza acest string
    :return: string
    """
    string = "Choose a command(s):\n" \
             "\tadd (book/client)\n" \
             "\tremove (book/client)\n" \
             "\tedit (book/client)\n" \
             "\tsearch (book/client)\n" \
             "\tlend (book)\n" \
             "\treturn (book)\n" \
             "\tprint (books/clients)\n" \
             "\tgenerate (books/clients)\n" \
             "\treports\n" \
             "\texit\n" \
             "Please do not specify 'book' for lend and return functions!\n" \
             "For multiple commands use ';' to separate them.\n" \
             "Command(s):"
    return string


class UserInterface:

    def __init__(self, book_service, client_service):
        self.__book_service = book_service
        self.__client_service = client_service
        self.__finished = False

    def getUserOptionInput(self):
        """
            Citeste comenzile din consola si apeleaza functiile corespunzatoare
        :return: -
        """
        commands = input()
        operations = commands.split(';')
        for operation in operations:
            if len(operation) == 0:
                return
            while operation[0] == ' ':
                operation = operation[1:]
            if operation.split()[0] in "add remove edit search print generate":
                try:
                    operation, option = operation.split(' ')
                except Exception:
                    print("Invalid operation!")
                    return
                if option in "book client":
                    try:
                        if option == "book":
                            entity = self.inputBookDetails(operation)
                            func = getattr(self.__book_service, operation)
                        elif option == "client":
                            entity = self.inputClientDetails(operation)
                            func = getattr(self.__client_service, operation)
                        else:
                            raise ValueError
                        result = func(entity)
                        if result is not None:
                            print(result)
                    except ValueError:
                        print("Invalid operation!")
                if option == "books":
                    if operation == "print":
                        print(self.__book_service.getAllBooks())
                    else:
                        print("How many books?\nn=", end="")
                        n = int(input())
                        self.__book_service.generate(n)
                elif option == "clients":
                    if operation == "print":
                        print(self.__client_service.getAllClients())
                    else:
                        print("How many clients?\nn=", end="")
                        n = int(input())
                        self.__client_service.generate(n)
            elif operation == "exit":
                self.__finished = True
            elif operation == "lend":
                book = self.__searchBook()
                client = self.__searchClient(book)
                self.__client_service.addBook(client, book)
                # self.__book_service.addClient(book, client)
            elif operation == "return":
                book = self.__searchBook()
                client = self.__searchClient(book)
                self.__client_service.removeBook(client, book)
                # self.__book_service.removeClient(book, client)
            elif operation == "reports":
                print("1. Most lent books\n"
                      "2. Clients sorted by number of lent books\n"
                      "3. First 20% most active clients\n"
                      "4. Average number of books lent by one client")
                n = int(input())
                match n:
                    case 1:
                        print(self.__book_service.getMostLentBooks())
                        self.__writeToFile(self.__book_service.getMostLentBooks())
                    case 2:
                        print(self.__client_service.getSortedClients())
                    case 3:
                        print(self.__client_service.getMostActiveClients())
                    case 4:
                        print(f'Average num of books lent by one client is {self.__client_service.getAverageBooks()}')
            else:
                print("Invalid command!")

    def __selectBook(self, books):
        """
        Afiseaza toate rezultatele cautarii si returneaza obiectul ales de utilizator
        :param books: list
        :return: book Object
        """
        print("Select book number:")
        for i in range(len(books)):
            print(f'\t#{i}: {books[i].getTitle()} - {books[i].getAuthor()}')
        try:
            option = int(input())
            return books[option]
        except ValueError:
            print("Invalid number!")
            return self.__selectBook(books)

    def __searchBook(self):
        """
        Cauta toate cartile cu numele dat in baza de date
        :return: book Object
        """
        print("Search book to lend:")
        book = self.inputBookDetails("search")
        book = self.__book_service.search(book, 'obj')
        if book is None:
            print("No books found.")
            return None
        if len(book) == 1:
            return book[0]
        else:
            return self.__selectBook(book)

    def __selectClient(self, clients):
        """
        Afiseaza toate rezultatele cautarii si returneaza obiectul ales de utilizator
        :param clients: list
        :return: client Object
        """
        print("Select client number:")
        for i in range(len(clients)):
            print(f'\t#{i}: {clients[i].getName()} - {clients[i].getCnp()}')
        try:
            option = int(input())
            return clients[option]
        except ValueError:
            print("Invalid number!")
            return self.__selectClient(clients)

    def __searchClient(self, book):
        """
        Cauta toti clientii cu numele dat in baza de date
        :param book: book Object
        :return: client Object
        """
        print(f'Search client to lend book #{book.getId()}:')
        client = self.inputClientDetails("search")
        client = self.__client_service.search(client, 'obj')
        if client is None:
            print("No clients found.")
            return None
        if len(client) == 1:
            return client[0]
        else:
            return self.__selectClient(client)

    def __writeToFile(self, report):
        with open("report.txt", "w") as f:
            f.write(report)

    def inputBookDetails(self, operation):
        """
            Citeste detaliile unor carti de la consola
        :param operation: string
        :return: Book object
        """
        input_id = -1
        title, description, author = "None", "None", "None"
        if operation not in "search add":
            print("id: ", end="")
            try:
                input_id = int(input())
                if input_id < 0:
                    raise ValueError
            except ValueError:
                print("Invlaid id!")
                return self.inputBookDetails(operation)
        if operation in "add edit search":
            print("title: ", end="")
            try:
                title = input()
                if title == "":
                    raise ValueError
            except ValueError:
                print("Invalid title!")
                return self.inputBookDetails(operation)
        if operation in "add edit":
            print("description: ", end="")
            try:
                description = input()
                if len(description) < 10:
                    raise ValueError
            except ValueError:
                print("Invalid description. PLease enter at least 10 characters!")
                return self.inputBookDetails(operation)
            print("author: ", end="")
            try:
                author = input()
                if len(author) < 2:
                    raise ValueError
            except ValueError:
                print("Invalid author. Please enter at least 2 characters!")
                return self.inputBookDetails(operation)
        book = Book(input_id, title, description, author)
        return book

    def inputClientDetails(self, operation):
        """
            Citeste detaliile unor clienti de la consola
        :param operation: string
        :return: Client object
        """
        input_id, cnp = -1, -1
        name = ""
        if operation not in "search add":
            print("id: ", end="")
            try:
                input_id = int(input())
                if input_id < 0:
                    raise ValueError
            except ValueError:
                print("Invlaid id!")
                return self.inputClientDetails(operation)
        if operation in "add edit search":
            print("name: ", end="")
            try:
                name = input()
                if name == "" or name.isdecimal():
                    raise ValueError
            except ValueError:
                print("Invalid name!")
                return self.inputClientDetails(operation)
        if operation in "add edit":
            print("cnp: ", end="")
            try:
                cnp = int(input())
                if cnp // 1000000000000 not in range(1, 6):
                    raise ValueError
            except ValueError:
                print("Invalid CNP!")
                return self.inputClientDetails(operation)

        client = Client(input_id, name, cnp)
        return client

    def run(self):
        """
        Afiseaza functionalitatile si citeste comenzile din consola pana cand se cere iesirea din program
        :return: -
        """
        while not self.__finished:
            print(printOptions())
            self.getUserOptionInput()
            time.sleep(3)
        return 0

    def __str__(self):
        return printOptions()
