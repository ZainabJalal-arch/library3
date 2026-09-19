from library import Book, EBook, Library, is_valid_isbn


def main():
    library = Library()

    book1 = Book(
        "Harry Potter",
        "J.K. Rowling",
        "1234567890"
    )

    book2 = Book(
        "The Hobbit",
        "J.R.R. Tolkien",
        "2345678901"
    )

    book3 = Book(
        "1984",
        "George Orwell",
        "3456789012"
    )

    ebook1 = EBook(
        "Python Basics",
        "John Smith",
        "4567890123",
        5.5
    )

    ebook2 = EBook(
        "Clean Code",
        "Robert Martin",
        "5678901234",
        8.2
    )

    # Add books
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(ebook1)
    library.add_book(ebook2)

    # Checkout book
    print("\n--- Checkout Book ---")
    library.checkout_book("1234567890")

    # Return book
    print("\n--- Return Book ---")
    library.return_book("2345678901")

    # Available books using filter + lambda
    print("\n--- Available Books (filter + lambda) ---")
    available_books = library.list_available_books()

    for book in available_books:
        print(book.describe())

    # Sort books using sorted + lambda
    print("\n--- Sorted Books (sorted + lambda) ---")
    all_books = library.get_all_books()

    sorted_books = sorted(
        all_books,
        key=lambda book: book.title
    )

    for book in sorted_books:
        print(book.title)

    # Get titles using map + lambda
    print("\n--- Book Titles (map + lambda) ---")

    titles = list(
        map(lambda book: book.title, all_books)
    )

    print(titles)

    # ISBN Validation
    print("\n--- ISBN Validation ---")
    print(is_valid_isbn("1234567890"))
    print(is_valid_isbn("12345"))

    # Find book
    print("\n--- Find Book ---")
    found_book = library.find_book("3456789012")

    if found_book:
        print(found_book.describe())
    else:
        print("Book not found.")

main()
print("f") 