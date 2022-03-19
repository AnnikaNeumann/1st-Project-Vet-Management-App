from db.run_sql import run_sql

from modules.animal import Animal
from modules.owner import Owner
from modules.vet import Vet

import repositories.owner_repo as owner_repo
import repositories.vet_repo as vet_repo


def save(animal):
    sql = "INSERT INTO books (title, genre, language, author, release) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.breed, animal.treatment]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 

def select_all():
    animal = []
    sql = "SELECT * FROM book"
    results = run_sql(sql) 
    for row in results:
        animal = Animal(row['name'], row ['dob'], row ['breed'], row ['treatment'], row ['owner_id'])
    return animal