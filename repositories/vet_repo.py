from db.run_sql import run_sql

from modules.animal import Animal
from modules.owner import Owner

import repositories.owner_repo as owner_repo
import repositories.animal_repo as animal_repo


def save(animal):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING *"
    values = [animal.name, animal.dob, animal.breed, animal.treatments, animal.owner_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal 