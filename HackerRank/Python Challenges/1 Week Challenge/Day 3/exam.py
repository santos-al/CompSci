

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
            count += 1


print(palindromeIndex("aaa"))
print(palindromeIndex("aab"))
print(palindromeIndex("baa"))

def palindromeIndexCorrect(s):
    # Two pointers to compare characters from both ends
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Check if removing the left character makes it a palindrome
            if s[left + 1:right + 1] == s[left + 1:right + 1][::-1]:
                return left
            # Check if removing the right character makes it a palindrome
            elif s[left:right] == s[left:right][::-1]:
                return right
            # If neither removal works, return -1 (shouldn't happen per problem constraints)
            else:
                return -1
        left += 1
        right -= 1

    # If no mismatch is found, the string is already a palindrome
    return -1