from db.run_sql import run_sql
from models.staff import Staff

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)

def save(staff):
    sql = 'INSERT INTO staff (name, start_date, department, performance) VALUES (%s, %s, %s, %s) RETURNING *'
    values = [staff.name, staff.start_date, staff.department, staff.performance]
    result = run_sql(sql, values)
    staff.id = result[0]['id']
    return staff