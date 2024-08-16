"""
Exercise 7: Book Class

Create a Book class with attributes title, author, and pages.
Add a method description() that returns a string with the book’s title and author.
Create a few Book objects and print their descriptions.
"""


class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return "Tile: " + self.title + ' - ' "Other: " + self.author


book = book("Bobby", "Kenfack Bodeler", 100)

print(book.description())
