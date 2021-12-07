from models.staff import Staff

import repositories.staff_repository as staff_repo

staff_repo.delete_all()


staff1 = Staff('Andrew', '02/05/2021', 'Keepers', 5)
staff_repo.save(staff1)

staff2 = Staff('Joe Exotic', '20/03/2020', 'Keepers', 1)
staff_repo.save(staff2)

res = staff_repo.list_all()

for staff in res:
    print(staff.__dict__)