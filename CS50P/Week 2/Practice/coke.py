"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts 
coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, 
one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
output how many cents in change the user is owed. Assume that the user will only input integers, 
and ignore any integer that isn’t an accepted denomination.
"""

def main():
    print("Welcome, please insert payment for a coke")
    total = coke_machine()
    print("Change Owed:", (-total))

def coke_machine():
    acceptable_coins = [5, 10, 25]
    total = 50
    payment = 0
    while (total > 0):
        print("Amount Due:", total)
        payment = int(input("Insert coin: "))
        if (payment in acceptable_coins):
            total -= payment
        else:
            continue
    return total


main()
