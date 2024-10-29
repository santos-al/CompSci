
i = 0
while (i < 4):
    print("Meow")
    i += 1

print('-------------------------------------------------------------')

basic_list = [0, 1, 2]
for i in basic_list:
    print("Purr")

print('-------------------------------------------------------------')


for _ in range(3):
    print("Meow again")

print('-------------------------------------------------------------')

print("Meow again again\n" * 3, end="")

print('-------------------------------------------------------------')

# while True:
#     n = int(input("What's n? "))
#     if(n > 0):
#         break

# for _ in range(n):
#     print("Meow meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
         n = int(input("What's n? "))
         if n > 0:
             break
    return n


def meow(n):
    for _ in range(n):
        print("Meow, meow, meow")

main()