class Book:
    def init(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def describe(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def init(self, title, author, isbn, file_size_mb, is_available=True):
        super().init(title, author, isbn, is_available)
        self.file_size_mb = file_size_mb

    def describe(self):
        return f"EBook: {self.title} by {self.author} - {self.file_size_mb} MB"


class Library:
    def init(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def remove_book(self, isbn):
        book = self.find_book(isbn)

        if book:
            self.books.remove(book)
            print(f"Book '{book.title}' removed successfully.")
        else:
            print("Book not found.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def checkout_book(self, isbn):
        book = self.find_book(isbn)

        if book is None:
            print("Book not found.")
        elif not book.is_available:
            print(f"Book '{book.title}' is already checked out.")
        else:
            book.is_available = False
            print(f"Book '{book.title}' checked out successfully.")

    def return_book(self, isbn):
        book = self.find_book(isbn)

        if book is None:
            print("Book not found.")
        else:
            book.is_available = True
            print(f"Book '{book.title}' returned successfully.")

    def list_available_books(self):
        return list(
            filter(lambda book: book.is_available, self.books)
        )

    def get_all_books(self):
        return self.books


def is_valid_isbn(isbn):
    return len(isbn) == 10 and isbn.isdigit()