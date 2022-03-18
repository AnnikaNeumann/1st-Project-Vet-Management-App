DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    language VARCHAR(255),
    author VARCHAR(255),
    release INT
);

CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    country VARCHAR(255)
);


INSERT INTO book (title, genre, language, author, release);
VALUES ('IT', 'Horror', 'English', 'Stephen King', 1988);

INSERT INTO authors (name, age, country);
VALUES ('Stephen King', 74, 'USA');


SELECT * FROM books;