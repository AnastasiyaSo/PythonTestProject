"""Homework 21_1"""
import pytest
from homework.homework_21.test_data_21_1 import create_books, create_clients
from homework import logger_module


@pytest.fixture(scope="module")
def setup_books_and_clients():
    """Creating and deleting books and clients"""
    books = create_books()
    clients = create_clients()
    yield books, clients
    del books
    del clients


def test_verify_client_can_take_book(setup_books_and_clients):
    """Check that a client can take a book"""
    books, clients = setup_books_and_clients
    assert clients["client_4"].take_book(books["book_5"]) is True
    logger_module.logger.info("%s %s can take book: %s",
                              clients["client_4"].first_name,
                              clients["client_4"].last_name,
                              books["book_5"].name_book)


def test_verify_client_can_reserve_book(setup_books_and_clients):
    """Check that a client can reserve a book"""
    books, clients = setup_books_and_clients
    assert clients["client_4"].take_book(books["book_6"]) is True
    logger_module.logger.info("%s %s can take book: %s",
                              clients["client_4"].first_name,
                              clients["client_4"].last_name,
                              books["book_6"].name_book)
    assert clients["client_5"].take_book(books["book_6"]) is True
    logger_module.logger.info("%s is read by another client. %s %s can "
                              "reserve the book", books["book_6"].name_book,
                              clients["client_5"].first_name,
                              clients["client_5"].last_name)
    assert clients["client_5"].reserve_book(books["book_6"]) is True
    logger_module.logger.info("%s is reserved successfully",
                              books["book_6"].name_book)


def test_verify_client_can_not_take_and_reserve_book(setup_books_and_clients):
    """Check that a client can not take and reserve a book if it is taken
             and reserved another client"""
    books, clients = setup_books_and_clients
    assert clients["client_4"].take_book(books["book_7"]) is True
    logger_module.logger.info("%s %s can take book: %s",
                              clients["client_4"].first_name,
                              clients["client_4"].last_name,
                              books["book_7"].name_book)
    assert clients["client_5"].reserve_book(books["book_7"]) is True
    logger_module.logger.info("%s is reserved successfully",
                              books["book_7"].name_book)
    assert clients["client_6"].take_book(books["book_7"]) is False
    logger_module.logger.info("%s is read by another client. %s %s can "
                              "not reserve the book",
                              books["book_7"].name_book,
                              clients["client_6"].first_name,
                              clients["client_6"].last_name)


def test_verify_client_can_return_book(setup_books_and_clients):
    """Check that a client can return a book"""
    books, clients = setup_books_and_clients
    assert clients["client_4"].take_book(books["book_8"]) is True
    logger_module.logger.info("%s %s can take book: %s",
                              clients["client_4"].first_name,
                              clients["client_4"].last_name,
                              books["book_8"].name_book)
    assert clients["client_4"].return_book(books["book_8"]) is True
    logger_module.logger.info("%s %s can return book: %s",
                              clients["client_4"].first_name,
                              clients["client_4"].last_name,
                              books["book_8"].name_book)


def test_verify_book_can_not_be_returned(setup_books_and_clients):
    """Check that a book can not be returned if it was not taken"""
    books, clients = setup_books_and_clients
    assert clients["client_6"].return_book(books["book_9"]) is False
    logger_module.logger.info("Book: %s is not taken",
                              books["book_9"].name_book)


def test_verify_client_can_not_return_book_that_they_did_not_take(
        setup_books_and_clients):
    """Check that a client can not return a book that they did not take"""
    books, clients = setup_books_and_clients
    assert clients["client_6"].take_book(books["book_10"]) is True
    logger_module.logger.info("%s %s can take book: %s",
                              clients["client_6"].first_name,
                              clients["client_6"].last_name,
                              books["book_10"].name_book)
    assert clients["client_5"].return_book(books["book_10"]) is False
    logger_module.logger.info("Book: %s is not taken by %s %s",
                              books["book_10"].name_book,
                              clients["client_5"].first_name,
                              clients["client_5"].last_name)
