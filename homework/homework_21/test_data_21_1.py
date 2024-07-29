"""Test data 21_1"""
from homework.homework_11 import homework_11_1


def create_books():
    """Creating books"""
    return {
        "book_5": homework_11_1.Book("Harry Potter 3", "J. K. Rowling", 5),
        "book_6": homework_11_1.Book("Harry Potter 4", "J. K. Rowling", 6),
        "book_7": homework_11_1.Book("Harry Potter 5", "J. K. Rowling", 7),
        "book_8": homework_11_1.Book("Harry Potter 6", "J. K. Rowling", 8),
        "book_9": homework_11_1.Book("Harry Potter 7", "J. K. Rowling", 9),
        "book_10": homework_11_1.Book("The Lord of the Ring 3",
                                      "J. R. R. Tolkien", 10)
    }


def create_clients():
    """Creating clients"""
    return {
        "client_4": homework_11_1.Client(4, "Peter", "Ivanov"),
        "client_5": homework_11_1.Client(5, "Ivan", "Petrov"),
        "client_6": homework_11_1.Client(6, "Anna", "Shyshkina")
    }
