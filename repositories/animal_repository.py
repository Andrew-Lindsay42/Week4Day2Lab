from db.run_sql import run_sql
from models.animal import Animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)