from model.Book import Book
from functions import generator


class BookService:

    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def add(self, book):
        """
        Adaugare carte
        :param book: object
        :return: -
        """
        book = Book(-1, book.getTitle(), book.getDescription(), book.getAuthor())
        self.__validator.validateBook(book)
        self.__repo.addBook(book)

    def edit(self, book):
        """
        Editare carte
        :param book: object
        :return: -
        """
        book = Book(book.getId(), book.getTitle(), book.getDescription(), book.getAuthor())
        self.__validator.validateBook(book)
        self.__repo.editBook(book)

    def remove(self, book):
        """
        Stergere carte
        :param book: object
        :return: -
        """
        book = Book(book.getId())
        self.__validator.validateBook(book)
        self.__repo.removeBook(book)

    def search(self, book, return_type="str"):
        """
        Cautare carte
        :param book: object
        :param return_type: string
        :return: string if return_type == "str" else list
        """
        bookString = []
        book = Book(-1, title=book.getTitle())
        self.__validator.validateBook(book)
        books = self.__repo.getBook(book)
        if return_type != "str":
            return books
        if books is not None:
            for book in books:
                bookString.append(f'#{book.getId()}: {book.getTitle()} - {book.getAuthor()}\n\t{book.getDescription()}')
            return '\n'.join(bookString)
        return "No books found."

    def generate(self, num):
        """
        Genereaza num carti dupa care le adauga in baza de date
        :param num: int
        :return: last book generated
        """
        generated_books = generator.generateBooks(num)
        lastBook = None
        for book in generated_books:
            self.add(book)
            lastBook = book

        return lastBook

    def getAllBooks(self):
        """
        Returneaza toate cartile din baza de date formatata ca string
        :return: string
        """
        booksString = []
        books = self.__repo.getAllBooks()
        for book in books:
            booksString.append(f'#{book.getId()}: {book.getTitle()} - {book.getAuthor()}\n\t{book.getDescription()}')
        return '\n\n'.join(booksString) if len(booksString) > 0 else 'No books registered in database.'

    def getMostLentBooks(self):
        """
        Returneaza un string cu primele 3 cele mai inchiriate carti
        :return: string
        """
        bList = self.__repo.getMostLentBooks()
        string = f'#1: {bList[0].getTitle()} - {bList[0].getAuthor()}\n' \
                 f'#2: {bList[1].getTitle()} - {bList[1].getAuthor()}\n' \
                 f'#3: {bList[2].getTitle()} - {bList[2].getAuthor()}'

        return string
