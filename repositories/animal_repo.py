from db.run_sql import run_sql

from modules.animal import Animal

def save(animal):
    sql = "INSERT INTO animals (name, dob, breed, treatments, owner_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.breed, animal.treatments, animal.owner_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 

def select_all():
    animal = []
    sql = "SELECT * FROM book"
    results = run_sql(sql) 
    for row in results:
        animal = Animal(row['name'], row ['dob'], row ['breed'], row ['treatments'], row ['owner_id'])
    return animal

    