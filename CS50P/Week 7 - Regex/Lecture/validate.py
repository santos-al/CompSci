import re

email = input("What's your email? ").strip()

# if ("@" in email and "." in email):
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# if ((username) and (domain.endswith(".edu"))):
#     print("Valid")
# else:
#     print("Invalid")

if re.search(r"^(\w|\s)+@(\w+\)?\w+\.(edu|com|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

