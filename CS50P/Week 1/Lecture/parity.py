print('-------------------------------------------------------------')
def main(): 
    x = int(input("What is x? "))
    is_even(x)

def is_even(n): 
    return n % 2 == 0


main()