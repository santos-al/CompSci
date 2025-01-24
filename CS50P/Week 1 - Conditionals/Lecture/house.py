print('-------------------------------------------------------------')
print('-------------------------------------------------------------')

name = input("What is your name? ")

match name:
    case "Harry" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who??")