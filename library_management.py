class Book:
    def __init__(self,title,author):
        self.title = title 
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    def return_book(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books_collection = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books_collection.append(new_book)
        print(f"Added: '{title}' to the library collection!")
    
    def display_all_books(self):
        if not self.books_collection:
            print("The library is currently empty.")
            return
        print("\n--- Current Library Catalog ---")
        for book in self.books_collection:
            status = "available" if book.is_available else "checked out"
            print(f"Title: {book.title:<20} | Author: {book.author:<15} | Status: {status}")

    def borrow_book_by_title(self, search_title):
        for book in self.books_collection:
            if book.title.lower()== search_title.lower():
                if book.borrow_book():
                    print(f"Success! You have borrowed '{book.title}'.")
                    return True
                else:
                    print(f"Sorry, '{book.title}' is already checked out!")
                    return False
        print(f"Error: '{search_title}' is not in the library collection.")
        return False




library = Library()


library.add_book("The Hobbit", "J.R.R. Tolkien")
library.add_book("1984", "George Orwell")

# View initial catalog state
library.display_all_books()

print("\n--- Processing Checkout Requests ---")
#  First checkout attempt 
library.borrow_book_by_title("1984")

# Second checkout attempt on the same book (Should catch that it's gone)
library.borrow_book_by_title("1984")

# Try to borrow a book that doesn't exist in our catalog
library.borrow_book_by_title("Harry Potter")

# View final catalog state to confirm the status flipped dynamically
library.display_all_books()
