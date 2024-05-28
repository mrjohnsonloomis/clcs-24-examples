def string_reverse(s):
    if s == '':
        return s
    elif len(s) == 1:
        return s
    else:
        first_char = s[0]
        rest_of_string = s[1:]
        reversed_rest = string_reverse(rest_of_string)
        return reversed_rest + first_char

print(string_reverse('hello'))