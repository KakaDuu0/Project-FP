# from repo.repository import Repository
import unittest
from tests.test import TestBook
from tests.test import TestClient
from tests.test import TestClientService
from tests.test import TestBookService
from tests.test import TestGenerator
from tests.test import TestRepository

from repo.file_repository import FileRepository
from service.book_service import BookService
from service.client_service import ClientService
from functions.validator import Validator
from ui.ui import UserInterface

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
        Functia main
    """

    filename_c = "clients.txt"
    filename_b = "books.txt"
    repo = FileRepository(filename_c, filename_b)
    validator = Validator()
    book_service = BookService(repo, validator)
    client_service = ClientService(repo, validator)
    ui = UserInterface(book_service, client_service)
    ui.run()
    unittest.main(exit=True)
