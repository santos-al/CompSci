import csv

path = "/Users/santosal/Desktop/Code/CompSci/CS50P/Week 6 - File I-O/Lecture"

name = input("What's your name? ")
home = input("Where's your home? ")

with open(path + "/students_input.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home" : home, "name" : name})

