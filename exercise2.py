class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __str__(self):
        return f'{self.book_name}, {self.book_code}, {self.book_price}, {self.book_year}, {self.book_author}'

    def __repr__(self):
        return f'{self.book_name}, {self.book_code}, {self.book_price}, {self.book_year}, {self.book_author}'

    def __lt__(self, other):
        return self.book_name < other.book_name

book1 = Book("Space", 1, 20, 2020, 'Slavi')
book2 = Book("Planet", 2, 22, 2021, 'Slavi')
book3 = Book("Bulgaria", 3, 15, 2022, 'Kiri')
book4 = Book("Plane", 4, 16, 2010, 'Ivan')

books = [book1, book2, book3, book4]

def sortName():
    print(sorted(books, reverse=True))

def author(author_name):
    for book in books:
        if book.book_author == author_name:
            print(book)

def search_book(book_code):
    for book in books:
        if book.book_code == book_code:
            print(book.book_year)
            return
    print('The book is not found!')

sortName()
author('Slavi')
search_book(4)