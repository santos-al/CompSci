"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, 
one per line, until the user inputs control-d (which is a common way of ending one’s 
input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
Treat the user’s input case-insensitively.
"""

def main():
    grocery_list()


def grocery_list():
    food_list = {}
    while(True):
        try:
            item = input().strip().upper()
            if (item in food_list):
                food_list[item] += 1
            else:
                food_list[item] = 1
        except EOFError:
            food_list_keys = list(food_list.keys())
            food_list_keys.sort()
            sorted_food_list = {i: food_list[i] for i in food_list_keys}
            for food in sorted_food_list:
                print(f"{sorted_food_list[food]} {food}")
            return


main()
