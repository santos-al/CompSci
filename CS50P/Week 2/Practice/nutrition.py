"""
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that 
“show nutrition information for the 20 most frequently consumed raw fruits … in the United States. 
Retail stores are welcome to download the posters, print, display and/or distribute them to consumers 
in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit 
(case-insensitively) and then outputs the number of calories in one portion of that fruit, per the 
FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will 
input fruits exactly as written in the poster (e.g., strawberries, not strawberry). 
Ignore any input that isn’t a fruit.
"""

def main():
    fruit_calories()

def fruit_calories():
    fruit = input("Item: ").lower()
    fruits_and_calories = {"apple" : "130",
                           "avocado" : "50",
                           "sweet cherries" : "100",
                           "kiwifruit" : "90",
                           "pear" : "100"
    }

    try:
        print("Calories:", fruits_and_calories[fruit])
    except:
        ...

main()
