class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Name: {self.title}, Author: {self.author}"


book1 = Book(title="Crime and Punishment", author="F. M. Dostoevsky")

print(book1.get_info())
