import re

name = input("What's your name? ").strip()


# You can both assign a value and ask a boolean
if matches := re.search(r"^(.+), (.+)$", name):
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")

