from models.staff import Staff

import repositories.staff_repository as staff_repo

staff_repo.delete_all()


staff1 = Staff('Andrew', '02/05/2021', 'Keepers', 5)
staff_repo.save(staff1)
