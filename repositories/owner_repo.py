from db.run_sql import run_sql

from modules.owner import Owner
from modules.animal import Animal


def save(owner):
    sql = "INSERT INTO owners (first_name, last_name, phone) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.first_name, owner.last_name, owner.phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner 


def select_last_name(last_name):
    owners = []
    sql = "SELECT last_name FROM owners WHERE last_name = %s"
    results = run_sql(sql) 
    for row in results:
        owner = Owner(row['first_name'], row ['last_name'], row ['phone'], row['id'])
        owners.append(owner)
    return owners


def select_animal(owner_id):
    animals = []
    sql = "SELECT owner_id FROM animals WHERE owner_id = %s"
    results = run_sql(sql) 
    for row in results:
        animal = Animal(row['name'], row ['DOB'], row ['breed'], row['treatments'])
        animals.append(animal)
    return animals