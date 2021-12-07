from db.run_sql import run_sql
from models.animal import Animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def save(animal):
    sql = "INSERT INTO animals (name, type, staff_id) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.staff.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal