def count_vowels(s):
    vowels = "aeiouAEIOU"
    # Base case: if the string is empty, return 0
    if s == "":
        return 0
    # Recursive case: check the first character and count it if it is a vowel, then count the rest
    else:
        if s[0] in vowels:
            return 1 + count_vowels(s[1:])
        else:
            return count_vowels(s[1:])

print(count_vowels('babiesaa'))