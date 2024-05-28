











def is_p(s):
    if s == '' or len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return is_p(s[1:-1])
    else:
        return False

print(is_p('hello'))
print(is_p('racecar'))