import sys


print('-------------------------------------------------------------')
print()
# Check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")


# Print name tags
# print("Hello, my name is", sys.argv[1])


print('-------------------------------------------------------------')
print()


if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)


print()
print('-------------------------------------------------------------')