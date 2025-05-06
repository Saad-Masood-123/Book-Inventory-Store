-- Create a Stored Procedure to Get Book Details by Author
USE book_inventory;

DELIMITER //

CREATE PROCEDURE GetBooksByAuthor(IN author_name_input VARCHAR(255))
BEGIN
    SELECT id, title, quantity
    FROM books
    WHERE author = author_name_input;
END //

DELIMITER ;

-- Example Call
-- CALL GetBooksByAuthor('George Orwell');

-- Create another Stored Procedure to Update Book Quantity
DELIMITER //

CREATE PROCEDURE UpdateBookQuantity(IN book_id INT, IN new_quantity INT)
BEGIN
    UPDATE books
    SET quantity = new_quantity
    WHERE id = book_id;
END //

DELIMITER ;

-- Example Call
-- CALL UpdateBookQuantity(1, 20);
