DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS  vets;


CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(255)
);

CREATE TABLE vets (
    id  SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    species VARCHAR(255),
    treatments VARCHAR(255),
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) 
);

-- Adding owners to the database

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Annika', 'Neumann', '07812323345');

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Karin', 'Kaefer', '07959523258');

INSERT INTO owners (first_name, last_name, phone)
VALUES ('Anita', 'Howard', '07769034592');

-- Adding Vet to database

INSERT INTO vets (name, animal_id)
VALUES ('Mr Roger Rabbit', 1);

INSERT INTO vets (name, animal_id)
VALUES ('Mrs Mickey Mouse', 3);

--Adding animals to the database

INSERT INTO animals (name, dob, species, treatments,owner_id, vet_id)
VALUES ('Elliot', '11092011', 'Tabby_cat', 'Flea and Worm treatment', 1, 1);

INSERT INTO animals (name, dob, species, treatments, owner_id, vet_id)
VALUES ('Dexter', '12042010', 'Tabby_cat', 'Thyroid medication', 2, 2);

INSERT INTO animals (name, dob, species, treatments, owner_id, vet_id)
VALUES ('Kingston', '03072015', 'Chihuaha', 'Antidepressants', 3, 1);

INSERT INTO animals (name, dob, species, treatments, owner_id, vet_id)
VALUES ('Bridget', '07032019', 'Chicken','Supplements', 1, 2);



