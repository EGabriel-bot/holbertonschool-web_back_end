-- Task 0 We are all unique!
-- creates a table users
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    UNIQUE (id)
);
