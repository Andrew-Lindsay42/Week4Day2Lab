import datetime
from models.staff import Staff
from models.animal import Animal

import repositories.staff_repository as staff_repo
import repositories.animal_repository as animal_repo

# Delete all existing data in animals and staff tables.
animal_repo.delete_all()
staff_repo.delete_all()

print('\n')

# Create 3 new staff
staff1 = Staff('Stephen Irwin', datetime.date(1962, 2, 22), 'Down-under Zone', 5)
staff2 = Staff('Joe Exotic', datetime.date(2020, 3, 20), 'Big Cats', 1)
staff3 = Staff('Andrew', datetime.date(2021, 11, 15), 'Intern', 3)
staff_repo.save(staff1)
staff_repo.save(staff2)
staff_repo.save(staff3)

# List all staff
print('1) List of all staff:')

all_staff = staff_repo.list_all()
for person in all_staff:
   print(person.__dict__)

print('\n')

# Find a specific staff member
print('2) Find staff member "Stephen Irwin":')
print(staff_repo.find_staff(staff1.id).__dict__)

print('\n')

# Remove a specific staff member
print('3) Remove staff member: Andrew')
staff_repo.remove_staff(staff3.id)
all_staff = staff_repo.list_all()
for person in all_staff:
   print(person.__dict__)

print("Intern's been fired")
print('\n')

# Update a specific staff member
print('4) Update Stephen Irwin to Steve:')
staff1.name = 'Steve Irwin'
staff1.performance = 6
staff_repo.update(staff1)
print(staff_repo.find_staff(staff1.id).__dict__)

print('\n')

# Create 3 new animals
tiger = Animal('Tony', 'Tiger', staff2)
tiger2 = Animal('Shere Khan', 'Tiger', staff2)
pigeon = Animal('Paul', 'Feral Pigeon', staff1)
animal_repo.save(tiger)
animal_repo.save(tiger2)
animal_repo.save(pigeon)

# List all animals
print('5) List of all animals:')

all_animals = animal_repo.list_all()
for animal in all_animals:
   print(animal.__dict__)

print('\n')

# Find a specific animal
print('6) Find animal "Tony":')
print(animal_repo.find_animal(tiger.id).__dict__)

print('\n')

# List all animals being looked after by a member of staff
print('7) List all animals being "looked after" by Joe Exotic: ')
animals = staff_repo.animals_under_care(staff2)
for animal in animals:
    print(animal.__dict__)

print('\n')

# Find the member of staff looking after an animal
print('8) Find the keeper looking after Paul the pigeon: ')
print(animal_repo.find_keeper(pigeon).__dict__)

print('\n')

# Update an animal
print('9) Move Tony over to Steve Irwin: ')
tiger.staff = staff1
animal_repo.update(tiger)
print(animal_repo.find_animal(tiger.id).__dict__)

print('\n')

# Remove an animal
print("10) Why's there a pigeon in the zoo anyway?")
animal_repo.remove_animal(pigeon.id)
all_animals = animal_repo.list_all()
for animal in all_animals:
   print(animal.__dict__)

print('\n')