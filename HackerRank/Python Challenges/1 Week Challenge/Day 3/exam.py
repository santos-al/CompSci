

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    s_reversed = s[::-1]
    count = 0
    
    if s == s_reversed:
        return -1
    else:
        for letter in s: 
            new_s = s[:count] + s[count + 1:]

            if new_s == new_s[::-1]: 

                return count
            else:

                s = new_s[:count] + letter + new_s[count:]

            count += 1


print(palindromeIndex("aaa"))
print(palindromeIndex("aab"))
print(palindromeIndex("baa"))