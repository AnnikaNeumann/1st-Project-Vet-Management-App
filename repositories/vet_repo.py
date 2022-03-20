from db.run_sql import run_sql

from modules.animal import Animal
from modules.owner import Owner
from modules.vet import Vet

import repositories.owner_repo as owner_repo
import repositories.animal_repo as animal_repo

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['id'])
        vets.append(vet)

    return vets