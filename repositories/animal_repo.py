from db.run_sql import run_sql

from modules.animal import Animal

def save(animal):
    sql = "INSERT INTO animals (name, dob, species, treatments, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.species, animal.treatments, animal.owner.id, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 
    # this function can also be used to add a second animal

def select_all():
    animal = []
    sql = "SELECT * FROM book"
    results = run_sql(sql) 
    for row in results:
        animal = Animal(row['name'], row['dob'], row['species'], row['treatments'], row['owner_id'])
    return animal

def select_animal_by_owner(owner):
    animals = []
    sql = "SELECT * FROM animals WHERE owner_id = %s"
    value=[owner.id]
    value = vet_
    results = run_sql(sql,value) 
    for row in results:
        animal = Animal(row['name'], row['dob'], row['species'], row['treatments'], owner, vet, row['id'])
        animals.append(animal)
    return animals






    



