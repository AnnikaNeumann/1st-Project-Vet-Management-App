import pdb 
from db.run_sql import run_sql

from modules.animal import Animal
from modules.owner import Owner
from modules.vet import Vet

import repositories.animal_repo as animal_repo
import repositories.owner_repo as owner_repo
import repositories.vet_repo as vet_repo



# test repos in here with their function

def save(animal):
    sql = "INSERT INTO animals (name, dob, species, treatments, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.species, animal.treatments, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 
    # Function works when using it frontend

def select_all():
    animal = []
    sql = "SELECT * FROM book"
    results = run_sql(sql) 
    for row in results:
        animal = Animal(row['name'], row['dob'], row['species'], row['treatments'], row['owner_id'])
    return animal
    # Function let's me see all animals of the table in database/terminal


def select_animal_by_owner(owner):
    animals = []
    sql = "SELECT * FROM animals WHERE owner_id = %s"
    value=[owner.id]
    results = run_sql(sql,value) 
    for row in results:
        vet = vet_repo.select_by_id(row['vet_id'])
        animal = Animal(row['name'], row['dob'], row['species'], row['treatments'], owner, vet, row['id'])
        animals.append(animal)
    return animals
    # Function let's me see all animals of specific owner in frontend

def update(animal):
    sql = "UPDATE animals SET name =%s, dob= %s, species=%s, treatments=%s WHERE id = %s"
    values = [animal.name, animal.dob, animal.species, animal.treatments]
    result = run_sql(sql, values)
    return result 
    # function needs to be refactored

def update(owner):
    sql = "UPDATE owners SET first_name =%s, last_name = %s, phone=%s WHERE id = %s"
    values = [owner.first_name,owner.last_name,owner.phone,owner.id]
    result = run_sql(sql, values)
    return result
    

def select_last_name(last_name):
    owners = []
    sql = "SELECT * FROM owners WHERE last_name = %s"
    value = [last_name]
    results = run_sql(sql, value)
    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['phone'], row['id'])
        owners.append(owner)
    return owners
    # function let's me search for and also renders last name of owner in frontend