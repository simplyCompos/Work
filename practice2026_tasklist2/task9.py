class Book:
    def init(self, title):
        self.title = title


class Reader:
    def init(self, name):
        self.name = name

    def read(self, book):
        print(f"{self.name} reading book {book.title}")
