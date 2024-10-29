print('-------------------------------------------------------------')
print()

students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

print()
print('-------------------------------------------------------------')

