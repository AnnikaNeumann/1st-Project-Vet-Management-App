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

def select_by_id(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        owner = Owner(result['first_name'], result['last_name'], result['phone'], result['id'])
    return owner


def select_last_name(last_name):
    owners = []
    sql = "SELECT * FROM owners WHERE last_name = %s"
    value = [last_name]
    results = run_sql(sql, value)
    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['phone'], row['id'])
        owners.append(owner)
    return owners


