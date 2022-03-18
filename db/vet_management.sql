DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    breed VARCHAR(255),
    treatments VARCHAR(255),
);

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone INT,
    pet_id INT,
);

--Adding animals to the database

INSERT INTO animals (name, dob, breed, treatments);
VALUES ('Elliot', '11092011', 'Tabby_cat', 'Flea and Worm treatment');

INSERT INTO animals (name, dob, breed, treatments);
VALUES ('Dexter', '12042010', 'Tabby_cat', 'Thyroid medication');

INSERT INTO animals (name, dob, breed, treatments);
VALUES ('Kingston', '03072015', 'Chihuaha', 'antidepressants');

INSERT INTO animals (name, dob, breed, treatments);
VALUES ('Bridget', '07032019', 'Chicken', 'none');

-- Adding owners to the database

INSERT INTO owners (first_name, last_name, phone, pet_id);
VALUES ('Annika', 'Neumann', 07812323345, 1);

INSERT INTO owners (first_name, last_name, phone, pet_id);
VALUES ('Karin', 'Kaefer', 07959523258, 2);

INSERT INTO owners (first_name, last_name, phone, pet_id);
VALUES ('Anita', 'Howard', 07769034592, 3);


SELECT * FROM animals;