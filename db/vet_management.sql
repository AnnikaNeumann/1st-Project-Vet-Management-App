DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    breed VARCHAR(255),
    treatments VARCHAR(255),
    owner_id INT
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone INT
);

--Adding animals to the database

INSERT INTO animals (name, dob, breed, treatments)
VALUES ('Elliot', '11092011', 'Tabby_cat', 'Flea and Worm treatment');

INSERT INTO animals (name, dob, breed, treatments)
VALUES ('Dexter', '12042010', 'Tabby_cat', 'Thyroid medication');

INSERT INTO animals (name, dob, breed, treatments)
VALUES ('Kingston', '03072015', 'Chihuaha', 'antidepressants');

INSERT INTO animals (name, dob, breed, treatments)
VALUES ('Bridget', '07032019', 'Chicken', '');

-- Adding owners to the database

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Annika', 'Neumann', 07812323345);

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Karin', 'Kaefer', 07959523258);

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Anita', 'Howard', 07769034592);



SELECT * FROM animals;