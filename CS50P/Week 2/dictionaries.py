print('-------------------------------------------------------------')
print()

students = {"Hermione" : "Gryffindor", 
            "Harry" : "Gryffindor", 
            "Ron" : "Gyrffindor", 
            "Draco" : "Slytherin"
}

print(students["Hermione"])
print(students["Draco"])

print('-------------------------------------------------------------')

# Prints the keys
for student in students:
    print(student)

print('-------------------------------------------------------------')

# Prints the key value pair
for student in students:
    print(student, students[student], sep=" : ")

print()
print('-------------------------------------------------------------')