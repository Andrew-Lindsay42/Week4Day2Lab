import datetime
from db.run_sql import run_sql
from models.staff import Staff
from models.animal import Animal

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)

def save(staff):
    sql = 'INSERT INTO staff (name, start_date, department, performance) VALUES (%s, %s, %s, %s) RETURNING *'
    values = [staff.name, staff.start_date, staff.department, staff.performance]
    result = run_sql(sql, values)
    staff.id = result[0]['id']
    return staff

def list_all():
    staff_list = []
    sql = 'SELECT * FROM staff'
    result = run_sql(sql)

    for row in result:
        staff = Staff(row['name'], row['start_date'], row['department'], row['performance'], row['id'])
        staff_list.append(staff)
    return staff_list

def find_staff(id):
    staff = None
    sql = 'SELECT * FROM staff WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        staff = Staff(result['name'], result['start_date'], result['department'], result['performance'], result['id'])
    return staff

def remove_staff(id):
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(staff):
    sql = "UPDATE staff SET (name, start_date, department, performance) = (%s, %s, %s, %s) WHERE id = %s"
    values = [staff.name, staff.start_date, staff.department, staff.performance, staff.id]
    run_sql(sql, values)

def animals_under_care(staff):
    animals = []

    sql = "SELECT * FROM animals WHERE staff_id = %s"
    values = [staff.id]
    results = run_sql(sql, values)

    for row in results:
        animal = Animal(row['name'], row['type'], staff, row['id'] )
        animals.append(animal)
    return animals
