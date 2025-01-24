print('-------------------------------------------------------------')
print()

path = "/Users/santosal/Desktop/Code/CompSci/CS50P/Week 6 - File I-O/Lecture"

with open(path + "/names.txt", "r") as file:
    for line in file:
        print("Hello, ", line.rstrip())

print()
print('-------------------------------------------------------------')
print()

names = []

with open(path + "/names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("Hello, ", name)

print('-------------------------------------------------------------')