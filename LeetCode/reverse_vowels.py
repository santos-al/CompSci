def reverseVowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    i, j = 0, len(s) - 1
    chars = list(s)
    while i < j:
        if chars[i] in vowels and chars[j] in vowels:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        elif chars[i] in vowels:
            j -= 1
        elif chars[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1

    return "".join(chars)
