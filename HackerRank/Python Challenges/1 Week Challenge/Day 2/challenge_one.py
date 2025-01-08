def lonely_integer(a):
    # Write your code here
    unique = 0
    for num in a:
        unique ^= num 
    return unique
   
       
    

arr = [0, 0, 1, 2, 1]

print(lonely_integer(arr))