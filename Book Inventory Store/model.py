# model.py

import mysql.connector
from config import DB_CONFIG

class BookModel:
    def connect(self):
        return mysql.connector.connect(**DB_CONFIG)

    def get_all_books(self):
        conn = self.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()
        return books

    def get_book_by_id(self, book_id):
        conn = self.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM books WHERE id = %s', (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book

    def add_book(self, title, author, quantity):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)', (title, author, quantity))
        conn.commit()
        conn.close()

    def update_book(self, book_id, title, author, quantity):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET title = %s, author = %s, quantity = %s WHERE id = %s', (title, author, quantity, book_id))
        conn.commit()
        conn.close()

    def delete_book(self, book_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = %s', (book_id,))
        conn.commit()
        conn.close()
