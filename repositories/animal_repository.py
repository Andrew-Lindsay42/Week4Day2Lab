import datetime
from db.run_sql import run_sql
from models.animal import Animal
# from models.staff import Staff
from repositories.staff_repository import find_staff

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def save(animal):
    sql = "INSERT INTO animals (name, type, keeper) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.staff.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def list_all():
    animal_list = []
    sql = 'SELECT * FROM animals'
    result = run_sql(sql)

    for row in result:
        animal = Animal(row['name'], row['type'], row['keeper'], row['id'])
        animal_list.append(animal)
    return animal_list

def find_animal(id):
    animal = None
    sql = 'SELECT * FROM animals WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        animal = Animal(result['name'], result['type'], result['keeper'], result['id'])
    return animal

def find_keeper(animal):
    keeper = None

    sql = "SELECT * FROM animals WHERE id = %s"
    values = [animal.id]
    result = run_sql(sql, values)

    if result is not None:
        keeper = find_staff(result[0]['keeper'])
    return keeper

def remove_animal(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, type, keeper) = (%s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.type, animal.staff.id, animal.id]
    run_sql(sql, values)