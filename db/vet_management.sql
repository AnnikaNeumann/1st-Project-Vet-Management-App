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
    phone VARCHAR(255)
);

--Adding animals to the database

INSERT INTO animals (name, dob, breed, treatments,owner_id)
VALUES ('Elliot', '11092011', 'Tabby_cat', 'Flea and Worm treatment', 1);

INSERT INTO animals (name, dob, breed, treatments, owner_id)
VALUES ('Dexter', '12042010', 'Tabby_cat', 'Thyroid medication', 2);

INSERT INTO animals (name, dob, breed, treatments, owner_id)
VALUES ('Kingston', '03072015', 'Chihuaha', 'antidepressants', 3);

INSERT INTO animals (name, dob, breed, treatments, owner_id)
VALUES ('Bridget', '07032019', 'Chicken','', 1);

-- Adding owners to the database

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Annika', 'Neumann', '07812323345');

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Karin', 'Kaefer', '07959523258');

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Anita', 'Howard', '07769034592');



SELECT * FROM animals;