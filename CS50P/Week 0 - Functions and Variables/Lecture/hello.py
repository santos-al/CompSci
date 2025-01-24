# set user input to name and print hello plus the name input
name = input("What's your name? \n")

# Creates a f string
print(f"hello, {name}")

print('-------------------------------------------------------------')

# Clears out whitespaces and capitalizes each word 
name = name.strip().title()
print(name)

print('-------------------------------------------------------------')

first, last = name.split(" ")

personName = input("Whats ur name? ")

# Curly braces are optional, but the indentation is required
def sayHello(personName="world"): {
    print("Hello " + personName)
}

sayHello(personName)
sayHello()