print('-------------------------------------------------------------')
print()

def main():
    print(f"x is {get_int("What's x?")}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass

main()

print()
print('-------------------------------------------------------------')
