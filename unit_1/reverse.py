animal_string = input('Enter a list of animals, separated by a comma: ')
animal_list = animal_string.split(',')

animal_list = ['bird', 'dog', 'cat']

final = []
for animal in animal_list:
    final.insert(0, animal)

