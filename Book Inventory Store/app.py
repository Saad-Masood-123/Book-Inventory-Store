from flask import Flask, render_template, request, redirect, url_for, flash
from model import BookModel
from controller import BookController
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'supersecretkey'

book_model = BookModel()
book_controller = BookController(book_model)

# SMTP settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'saadchahal000@gmail.com'  # Replace
SMTP_PASSWORD = ''  # Replace

def send_email(subject, body, to=SMTP_USER):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SMTP_USER
        msg['To'] = to

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Email Error: {e}")

@app.route('/')
def index():
    books = book_controller.get_all_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    quantity = request.form['quantity']
    book_controller.add_book(title, author, int(quantity))
    send_email('Book Added', f'New Book "{title}" by {author} with {quantity} copies added.')
    flash('Book Added Successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/update/<int:book_id>', methods=['POST'])
def update_book(book_id):
    title = request.form['title']
    author = request.form['author']
    quantity = request.form['quantity']
    book_controller.update_book(book_id, title, author, int(quantity))
    send_email('Book Updated', f'Book "{title}" updated with {quantity} copies.')
    flash('Book Updated Successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book_controller.delete_book(book_id)
    send_email('Book Deleted', f'Book ID {book_id} deleted.')
    flash('Book Deleted Successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/buy/<int:book_id>', methods=['POST'])
def buy_book(book_id):
    email = request.form.get('email')
    book = book_model.get_book_by_id(book_id)

    if book and book['quantity'] > 0:
        new_quantity = book['quantity'] - 1
        book_controller.update_book(book_id, book['title'], book['author'], new_quantity)

        if email:
            send_email(
                subject='Book Purchase Confirmation',
                body=f'Thank you for purchasing "{book["title"]}". Remaining: {new_quantity} copies.',
                to=email
            )

        flash('Book Purchased Successfully!', 'success')
    else:
        flash('Book is out of stock!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
