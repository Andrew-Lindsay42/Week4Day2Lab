from models.staff import Staff
from models.animal import Animal

import repositories.staff_repository as staff_repo
import repositories.animal_repository as animal_repo

animal_repo.delete_all()
staff_repo.delete_all()

staff1 = Staff('Andrew', '02/05/2021', 'Keepers', 5)
staff2 = Staff('Joe Exotic', '20/03/2020', 'Keepers', 1)
staff_repo.save(staff1)
staff_repo.save(staff2)

tiger = Animal('Tony', 'Tiger', staff2)
tiger2 = Animal('Shere Khan', 'Tiger', staff2)
animal_repo.save(tiger)
animal_repo.save(tiger2)

# animal_repo.remove_animal(tiger2.id)

tiger.name = 'Fred'
tiger.staff = staff1
animal_repo.update(tiger)


# print(animal_repo.find_keeper(tiger2).__dict__)

# res = staff_repo.animals_under_care(staff2)
# for animal in res:
#     print(animal.__dict__)

# print(animal_repo.find_animal(tiger2.id).__dict__)

# staff_repo.remove_staff(staff2.id)

# staff1.name = 'Andrew Lindsay'
# staff1.performance = 6
# staff_repo.update(staff1)

# res = animal_repo.list_all()
# for animal in res:
#     print(animal.__dict__)