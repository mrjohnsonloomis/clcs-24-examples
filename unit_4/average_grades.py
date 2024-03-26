import matplotlib.pyplot as plt
import math

with open ('grades_by_term.txt') as file:
    data = file.readlines()

def average(listy: list):
    total = 0
    for num in listy:
        total += num
    return total/len(listy)

grades = {}
for row in data:
    row = row.strip()
    to_parse = row.split(',')
    if to_parse[0] in grades:
        grades[to_parse[0]].append(int(to_parse[1]))
    else:
        grades[to_parse[0]] = [int(to_parse[1])]

subjects = []
averages = []
for key, value in grades.items():
    subjects.append(key)
    averages.append(average(value))

print(subjects)

plt.bar(subjects, averages)
plt.show()