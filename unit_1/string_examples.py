sample = input('Enter a string to test out these cool string methods on!: ')

print(f'This is the string capitalized: {sample.capitalize()}')
print(f'This is the string lower: {sample.lower()}')
print(f'Is this string numeric?: {sample.isnumeric()}')

if sample.startswith('P'):
    print('okay, I see you like the letter P.')
else:
    print('Why not start with the letter P?')

print(f'{sample.split()}')
