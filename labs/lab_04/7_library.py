class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def add_book(self, book):
        self.book_list.append(book)
        return self.book_list

    def list_books(self):
        return self.book_list


books_list = []
library1 = Library(books_list)
library1.add_book("F. M. Dostoevsky — Crime and Punishment")

print(library1.list_books())
