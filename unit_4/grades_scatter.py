import matplotlib.pyplot as plt

with open('grades_by_subject.txt') as file:
    file.readline() # skip the header
    data = file.readlines()
x = []
y = []

for line in data:
    line = line.strip()
    to_parse = line.split(',')
    x.append(to_parse[0])
    y.append(int(to_parse[1]))

plt.scatter(x, y, color='red')
plt.show()