print('-------------------------------------------------------------')
print()

def main():
    print_column(3)
    print()
    print_row(4)
    print()
    print_square(8)


def print_column(height):
    for _ in range(height):
        print("#")

    # OR

    # print("#\n" * height, end="")


def print_row(width):
    print("?" * width)

def print_square(size):
    for _ in range(size):
        print("#" * (size * 2))

main()



print()
print('-------------------------------------------------------------')
