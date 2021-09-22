-- creates a table users
CREATE table IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email  VARCHAT(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
