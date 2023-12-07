list_parse = [1, 5, 9, 18, 10, 11, 36, 0, 13, 2, 1, 4, 5, 15]

string_parse = '''Four score and seven years ago, 
                our fathers brought forth to this land a new nation, 
                dedicated to the proposition that all men are created equal'''

for num in list_parse:
    print(num)

for letter in string_parse:
    print(letter)

for word in string_parse.split():
    print(word)

print(string_parse.split())