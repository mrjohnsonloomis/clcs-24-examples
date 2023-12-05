to_find = input('Enter a string to check: ')

if to_find.find('Python') != -1:
    print(f'there are {to_find.count("n")} n in the string.')
else:
    print('No match. ')
