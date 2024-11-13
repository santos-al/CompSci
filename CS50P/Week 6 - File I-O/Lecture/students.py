import csv

path = "/Users/santosal/Desktop/Code/CompSci/CS50P/Week 6 - File I-O/Lecture"

students = []

with open(path + "/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name" : row["name"], "home" : row["home"]})


# 'lambda is an anonymous function'
for student in sorted(students, key=lambda student: student["home"], reverse=True):
    print(f"{student['name']} is from {student['home']}")