
path = "/Users/santosal/Desktop/Code/CompSci/CS50P/Week 6 - File I-O/Lecture"

name = input("What's your name? ")

with open(path + "/names.txt", "a") as file:
    file.write(f"{name}\n") 

