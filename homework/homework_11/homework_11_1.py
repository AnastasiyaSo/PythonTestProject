"""Homework # 11"""
# Task #1


class Book:
    """Create class Book"""

    def __init__(self, name_book, author,
                 isbn):
        self.name_book = name_book
        self.author = author
        self.isbn = isbn
        self.is_reserved = False
        self.reserved_by = None
        self.is_taken = False
        self.taken_by = None


class Client:
    """Create class Client"""

    def __init__(self, client_id, first_name, last_name):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name

    def reserve_book(self, book):
        """Reserve book method"""
        if not book.is_reserved:
            book.is_reserved = True
            book.reserved_by = self.client_id
            print(f"\"{book.name_book}\" is reserved successfully")
            return True
        print(f"\"{book.name_book}\" is reserved by another client")
        return False

    def take_book(self, book):
        """Take book method"""
        if not book.is_taken and not book.is_reserved:
            book.is_taken = True
            book.taken_by = self.client_id
            print(f"You can take book: \"{book.name_book}\"")
            return True
        if (not book.is_taken and book.is_reserved
                and book.reserved_by == self.client_id):
            book.is_taken = True
            book.is_reserved = False
            book.reserved_by = None
            book.taken_by = self.client_id
            print(f"Book was returned. "
                  f"You can take reserved book: \"{book.name_book}\"")
            return True
        if book.is_taken and not book.is_reserved:
            print(f"Book: \"{book.name_book}\" is read by another"
                  f" client. You can reserve the book")
            return True
        if (book.is_taken and book.is_reserved
                and book.reserved_by != self.client_id):
            print(f"Book: \"{book.name_book}\" is read by another "
                  f"client and is not available for reserving")
            return False
        if (book.is_taken and book.is_reserved
                and book.reserved_by == self.client_id):
            print(f"Book: \"{book.name_book}\" is read by another "
                  f"client. Book \"{book.name_book}\" is reserved by you")
            return True
        return False

    def return_book(self, book):
        """Return book method"""
        if book.is_taken and book.taken_by == self.client_id:
            book.is_taken = False
            book.taken_by = None
            print(f"\"{book.name_book}\" is returned successfully")
            return True
        if book.is_taken and book.taken_by != self.client_id:
            print(f"Error: \"{book.name_book}\" is not taken by you")
            return False
        print(f"Error: \"{book.name_book}\" is not taken")
        return False


if __name__ == "__main__":
    book_1 = Book("Harry Potter 1", "J. K. Rowling", 1)
    book_2 = Book("Harry Potter 2", "J. K. Rowling", 2)
    book_3 = Book("The Lord of the Ring 1", "J. R. R. Tolkien", 3)
    book_4 = Book("The Lord of the Ring 2", "J. R. R. Tolkien", 4)

    client_1 = Client(1, "Ivan", "Ivanov")
    client_2 = Client(2, "Vasya", "Petrov")
    client_3 = Client(3, "Olia", "Pupkina")

    assert client_1.take_book(book_1), True
    assert client_2.take_book(book_1), True
    assert client_2.reserve_book(book_1), True
    assert not client_3.take_book(book_1), False
    assert client_2.take_book(book_1), True
    assert not client_3.return_book(book_1), False
    assert not client_3.return_book(book_3), False
    assert client_1.return_book(book_1), True
