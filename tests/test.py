from repo.file_repository import FileRepository
from functions.validator import Validator
from model.Client import Client
from model.Book import Book
from service.book_service import BookService
from service.client_service import ClientService
from functions.generator import *
import unittest


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(1, title="Book 1", description="Description 1", author="Author 1")
        self.book2 = Book(2, title="Book 2", description="Description 2", author="Author 2")
        self.book3 = Book(3, title="Book 3", description="Description 3", author="Author 3")
        self.book1Copy = Book(4, title="Book 1", description="Description 1", author="Author 1")
        self.book1Copy.setId(self.book1.getId())

    def testGetId(self):
        self.assertEqual(self.book1.getId(), 1, "Should be 1")
        self.assertNotEqual(self.book3.getId(), 2, "Should be 3")
        self.assertEqual(self.book2.getId(), 2, "Should be 2")

    def testSetId(self):
        self.book2.setId(5)
        self.assertEqual(self.book2.getId(), 5, "Should be 5")

    def testEq(self):
        self.assertEqual(self.book1, self.book1Copy)
        self.assertNotEqual(self.book1, self.book3)

    def testGetTitle(self):
        self.assertEqual(self.book1.getTitle(), "Book 1")
        self.assertNotEqual(self.book2.getTitle(), "Book 1")

    def testSetTitle(self):
        self.book3.setTitle("New Title")
        self.assertEqual(self.book3.getTitle(), "New Title")

    def testGetDescription(self):
        self.assertEqual(self.book1.getDescription(), "Description 1")
        self.assertEqual(self.book3.getDescription(), "Description 3")

    def testSetDescription(self):
        self.book1.setDescription("New Description")
        self.assertEqual(self.book1.getDescription(), "New Description")


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client1 = Client(1, "Name 1", 1234567891234)
        self.client2 = Client(2, "Name 2", 5123467891234)
        self.client1Copy = Client(3, "Name 1", 1234567891234)
        self.client1Copy.setId(self.client1.getId())

    def testGetId(self):
        self.assertEqual(self.client1.getId(), 1, "Should be 1")
        self.assertNotEqual(self.client2.getId(), 1, "Should be 2")

    def testEq(self):
        self.assertEqual(self.client1, self.client1Copy)
        self.assertNotEqual(self.client1, self.client2)

    def testSetId(self):
        self.client2.setId(3)
        self.assertEqual(self.client2.getId(), 3)

    def testGetName(self):
        self.assertEqual(self.client2.getName(), "Name 2")
        self.assertEqual(self.client1.getName(), "Name 1")

    def testSetName(self):
        self.client2.setName("New Name")
        self.assertEqual(self.client2.getName(), "New Name")

    def testGetCnp(self):
        self.assertEqual(self.client1.getCnp(), 1234567891234)

    def testSetCnp(self):
        self.client2.setCnp(5030420303914)
        self.assertEqual(self.client2.getCnp(), 5030420303914)

    def testGetLentBooks(self):
        self.assertEqual(self.client2.getLentBooks(), [])

    def testLendBook(self):
        self.client2.lendBook("book")
        self.assertEqual(self.client2.getLentBooks(), ["book"])

    def testReturnBook(self):
        self.client2.returnBook("book")
        self.assertEqual(self.client2.getLentBooks(), [])


class TestClientService(unittest.TestCase):
    def setUp(self):
        self.__repo = FileRepository("c_test.txt", "b_test.txt")
        self.__validator = Validator()
        self.__client_service = ClientService(self.__repo, self.__validator)
        self.client1 = Client(0, "Name 1", 1234567891234)
        self.client2 = Client(1, "Name 2", 5123467891234)

    def testAddClient(self):
        self.__client_service.add(self.client1)
        self.assertNotEqual(self.__client_service.getAllClients(), "No clients registered in database.")

    def testEditClient(self):
        self.__client_service.edit(Client(0, "New Name", 1234567891234))
        self.assertEqual(self.__client_service.search(self.client1, "list"), None)

    def testDeleteClient(self):
        self.__client_service.remove(Client(0, "New Name", 1234567891234))
        self.assertEqual(self.__client_service.getAllClients(), "No clients registered in database.")

    def testGetAverageBook(self):
        self.assertEqual(self.__client_service.getAverageBooks(), 0)


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.__repo = FileRepository("c_test.txt", "b_test.txt")
        self.__validator = Validator()
        self.__book_service = BookService(self.__repo, self.__validator)
        self.book1 = Book(1, title="Book 1", description="Description 1", author="Author 1")
        self.book2 = Book(2, title="Book 2", description="Description 2", author="Author 2")

    def testAddBook(self):
        self.__book_service.add(self.book1)
        self.assertNotEqual(self.__book_service.getAllBooks(), "No books registered in database.")

    def testEditBook(self):
        self.__book_service.edit(Book(0, "New Book", "ahahahahhh", "Author 1"))
        self.assertEqual(self.__book_service.search(self.book1, "list"), None)

    def testRemoveBook(self):
        self.__book_service.remove(Book(0, "New Book", "ahahahahhh", "Author 1"))
        self.assertEqual(self.__book_service.getAllBooks(), "No books registered in database.")


class TestGenerator(unittest.TestCase):
    def testGenerateClient(self):
        self.assertNotEqual(generateClients(1), [])
        self.assertNotEqual(generateClientsRecursive(1, []), [])

    def testGenerateCnp(self):
        self.assertGreater(generateCnp(), 1000000000000)

    def testGenerateBooks(self):
        self.assertNotEqual(generateBooks(2), [])
        self.assertNotEqual(generateBooksRecursive(2, []), [])

    def testGenerateBooksBLACKBOX(self):
        self.assertNotEqual(generateBooks(2), [])
        self.assertNotEqual(generateBooksRecursive(2, []), [])


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.__repo = FileRepository("c_test.txt", "b_test.txt")
        self.book1 = Book(0, title="Book 1", description="Description 1", author="Author 1")
        self.client1 = Client(0, "Name 1", 1234567891234)
        self.__repo.addBook(self.book1)
        self.__repo.addClient(self.client1)

    def TestAddBookToClient(self):
        self.__repo.addBookToClient(self.book1, self.client1)
        self.assertEqual(self.__repo.getClient(self.client1).getLentBooks(), [self.book1])

    def TestRemoveBookFromClient(self):
        self.__repo.removeBookFromClient(self.book1, self.client1)
        self.assertEqual(self.__repo.getClient(self.client1).getLentBooks(), [])
