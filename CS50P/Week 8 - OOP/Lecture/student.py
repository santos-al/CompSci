def main():
    student = get_student()

    # Causes error because tuples are immutable
    if student[0] == "Padma":
        student[1] = "Ravenclaw"

    print(f"{student[0]} from {student[1]}")


# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")


if __name__ == "__main__":
    main()


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    
    return student

    # Returns a tuple (tuples are similar to lists but are immutable)
    # return (name, house)