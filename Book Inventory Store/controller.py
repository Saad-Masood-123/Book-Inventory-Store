# controller.py

class BookController:
    def __init__(self, model):
        self.model = model

    def get_all_books(self):
        return self.model.get_all_books()

    def add_book(self, title, author, quantity):
        self.model.add_book(title, author, quantity)

    def update_book(self, book_id, title, author, quantity):
        self.model.update_book(book_id, title, author, quantity)

    def delete_book(self, book_id):
        self.model.delete_book(book_id)
