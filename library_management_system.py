import json


class Book:

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available,
        }

    @staticmethod
    def from_dict(d):
        return Book(d["book_id"], d["title"], d["author"], d["available"])


class Member:

    def __init__(self, member_id, name, borrowed=None):
        self.member_id = member_id
        self.name = name
        self.borrowed = borrowed if borrowed is not None else []

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed": self.borrowed,
        }

    @staticmethod
    def from_dict(d):
        return Member(d["member_id"], d["name"], d["borrowed"])


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author):
        self.books.append(Book(book_id, title, author))

    def add_member(self, member_id, name):
        self.members.append(Member(member_id, name))

    def find_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        return None

    def find_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    def borrow(self, member_id, book_id):
        m = self.find_member(member_id)
        b = self.find_book(book_id)
        if m is None or b is None:
            return False, "Member or book not found"
        if not b.available:
            return False, "Book not available"
        b.available = False
        m.borrowed.append(book_id)
        return True, "Borrowed successfully"

    def return_book(self, member_id, book_id):
        m = self.find_member(member_id)
        b = self.find_book(book_id)
        if m is None or b is None:
            return False, "Member or book not found"
        if book_id not in m.borrowed:
            return False, "This member did not borrow this book"
        b.available = True
        m.borrowed.remove(book_id)
        return True, "Returned successfully"

    def to_json(self):
        return {
            "books": [b.to_dict() for b in self.books],
            "members": [m.to_dict() for m in self.members],
        }

    @staticmethod
    def from_json(d):
        lib = Library()
        lib.books = [Book.from_dict(b) for b in d.get("books", [])]
        lib.members = [Member.from_dict(m) for m in d.get("members", [])]
        return lib


def save_library(lib, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(lib.to_json(), f, indent=2)


def load_library(filename="data.json"):
    try:
        with open(filename) as f:
            data = json.load(f)
            return Library.from_json(data)
    except FileNotFoundError:
        return Library()


def run():
    lib = load_library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. Save & Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            bid = input("Book ID: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            lib.add_book(bid, title, author)
        elif choice == "2":
            mid = input("Member ID: ").strip()
            name = input("Name: ").strip()
            lib.add_member(mid, name)
        elif choice == "3":
            mid = input("Member ID: ").strip()
            bid = input("Book ID: ").strip()
            ok, msg = lib.borrow(mid, bid)
            print(msg)
        elif choice == "4":
            mid = input("Member ID: ").strip()
            bid = input("Book ID: ").strip()
            ok, msg = lib.return_book(mid, bid)
            print(msg)
        elif choice == "5":
            print("Books:")
            for b in lib.books:
                print(
                    f"{b.book_id}: {b.title} by {b.author} (Available: {b.available})"
                )
        elif choice == "6":
            print("Members:")
            for m in lib.members:
                print(f"{m.member_id}: {m.name} Borrowed: {m.borrowed}")
        elif choice == "7":
            save_library(lib)
            print("Library saved. Exiting.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run()
