"""Homework # 20.1"""
import unittest
from homework import logger_module
from homework.homework_11 import homework_11_1


class TestLibraryMethods(unittest.TestCase):
    """Check  library methods"""

    @classmethod
    def setUpClass(cls):
        cls.book_5 = homework_11_1.Book("Harry Potter 3", "J. K. Rowling", 5)
        cls.book_6 = homework_11_1.Book("Harry Potter 4", "J. K. Rowling", 6)
        cls.book_7 = homework_11_1.Book("Harry Potter 5", "J. K. Rowling", 7)
        cls.book_8 = homework_11_1.Book("Harry Potter 6", "J. K. Rowling", 8)
        cls.book_9 = homework_11_1.Book("Harry Potter 7", "J. K. Rowling", 9)
        cls.book_10 = homework_11_1.Book("The Lord of the Ring 3",
                                         "J. R. R. Tolkien", 10)

        cls.client_4 = homework_11_1.Client(4, "Peter", "Ivanov")
        cls.client_5 = homework_11_1.Client(5, "Ivan", "Petrov")
        cls.client_6 = homework_11_1.Client(6, "Anna", "Shyshkina")

    @classmethod
    def tearDownClass(cls):
        del cls.book_5
        del cls.book_6
        del cls.book_7
        del cls.book_8
        del cls.book_9
        del cls.book_10
        del cls.client_4
        del cls.client_5
        del cls.client_6

    def test_verify_client_can_take_book(self):
        """Check that a client can take a book"""
        self.assertTrue(self.client_4.take_book(self.book_5))
        logger_module.logger.info("%s %s can take book: %s",
                                  self.client_4.first_name,
                                  self.client_4.last_name,
                                  self.book_5.name_book)

    def test_verify_client_can_reserve_book(self):
        """Check that a client can reserve a book"""
        self.assertTrue(self.client_4.take_book(self.book_6))
        logger_module.logger.info("%s %s can take book: %s",
                                  self.client_4.first_name,
                                  self.client_4.last_name,
                                  self.book_6.name_book)
        self.assertTrue(self.client_5.take_book(self.book_6))
        logger_module.logger.info("%s is read by another client. "
                                  "%s %s can reserve the book",
                                  self.book_6.name_book,
                                  self.client_5.first_name,
                                  self.client_5.last_name)
        self.assertTrue(self.client_5.reserve_book(self.book_6))
        logger_module.logger.info("%s is reserved successfully",
                                  self.book_6.name_book)

    def test_verify_client_can_not_take_and_reserve_book(self):
        """Check that a client can not take and reserve a book if it is taken
         and reserved another client"""
        self.assertTrue(self.client_4.take_book(self.book_7))
        logger_module.logger.info("%s %s can take book: %s",
                                  self.client_4.first_name,
                                  self.client_4.last_name,
                                  self.book_7.name_book)
        self.assertTrue(self.client_5.reserve_book(self.book_7))
        logger_module.logger.info("%s is reserved successfully",
                                  self.book_7.name_book)
        self.assertFalse(self.client_6.take_book(self.book_7))
        logger_module.logger.info("%s is read by another client. "
                                  "%s %s can not reserve the book",
                                  self.book_7.name_book,
                                  self.client_6.first_name,
                                  self.client_6.last_name)

    def test_verify_client_can_return_book(self):
        """Check that a client can return a book"""
        self.assertTrue(self.client_4.take_book(self.book_8))
        logger_module.logger.info("%s %s can take book: %s",
                                  self.client_4.first_name,
                                  self.client_4.last_name,
                                  self.book_8.name_book)
        self.assertTrue(self.client_4.return_book(self.book_8))
        logger_module.logger.info("%s %s can return book: %s",
                                  self.client_4.first_name,
                                  self.client_4.last_name,
                                  self.book_8.name_book)

    def test_verify_book_can_not_be_returned(self):
        """Check that a book can not be returned if it was not taken"""
        self.assertFalse(self.client_6.return_book(self.book_9))
        logger_module.logger.info("Book: %s is not taken",
                                  self.book_9.name_book)

    def test_verify_client_can_not_return_book_that_they_did_not_take(self):
        """Check that a client can not return a book that they did not take"""
        self.assertTrue(self.client_6.take_book(self.book_10))
        logger_module.logger.info("%s %s can take book: %s",
                                  self.client_6.first_name,
                                  self.client_6.last_name,
                                  self.book_10.name_book)
        self.assertFalse(self.client_5.return_book(self.book_10))
        logger_module.logger.info("Book: %s is not taken by %s %s",
                                  self.book_8.name_book,
                                  self.client_5.first_name,
                                  self.client_5.last_name)
