-- Create a View for Books with quantity greater than 10
USE book_inventory;

CREATE OR REPLACE VIEW view_high_quantity_books AS
SELECT id, title, author, quantity
FROM books
WHERE quantity > 10;

-- Example Join: Assume another table for demonstration
CREATE TABLE IF NOT EXISTS authors_info (
    author_name VARCHAR(255) PRIMARY KEY,
    nationality VARCHAR(100)
);

INSERT INTO authors_info (author_name, nationality) VALUES
('George Orwell', 'British'),
('Jane Austen', 'British'),
('Fyodor Dostoevsky', 'Russian'),
('J.R.R. Tolkien', 'British'),
('Haruki Murakami', 'Japanese'),
('Leo Tolstoy', 'Russian'),
('Homer', 'Greek'),
('Colleen Hoover', 'American');

-- Inner Join between books and authors_info
SELECT b.id, b.title, b.author, a.nationality
FROM books b
INNER JOIN authors_info a ON b.author = a.author_name;
