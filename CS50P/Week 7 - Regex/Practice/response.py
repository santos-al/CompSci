"""
Response Validation
When creating a Google Form that prompts users for a short answer (or paragraph), 
it’s possible to enable response validation and require that the user’s input match a regular expression. For instance, 
you could require that a user input an email address with a regex like this one:

^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
Or you could more easily use Google’s built-in support for validating an email address, per the screenshot below, much like you could use a library in your own code:

Google Form

In a file called response.py, using either validator-collection or validators from PyPI, implement 
a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively, 
if the input is a syntatically valid email address. You may not use re. And do not validate whether the email address’s domain name actually exists.
"""

from validator_collection import validators




from validator_collection import validators

def main():
    print(check_email(input("What's your email address? ")))
    # print(check_email(test))

def check_email(email):
    try:
        if validators.email(email):
            return "Valid"
        else:
            return "Invalid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
