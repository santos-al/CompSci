"""
In Massachusetts, home to Harvard University, 
it’s possible to request a vanity license plate for your car,
 with your choice of letters and numbers instead of random ones. 
 Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … 
vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output 
Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s 
input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all 
requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional 
functions for is_valid to call (e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    punctuation = [",", ".", " ", "!", "?"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    was_there_a_number = False
    plate_stripped = plate.strip().upper()
    if (len(plate_stripped) < 2 or len(plate_stripped) > 6):
        return False
    else:
        if (plate_stripped[0] in number or plate_stripped[1] in number):
            return False
        else:
            for char in plate_stripped:
                if (char in punctuation):
                    return False
                else:
                    if (char in number):
                        if (not was_there_a_number):
                            if(char == "0"):
                                return False
                        was_there_a_number = True
                    if (was_there_a_number and char not in number):
                        return False
            return True


main()
