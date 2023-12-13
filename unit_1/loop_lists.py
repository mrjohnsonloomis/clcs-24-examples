listy = [1, 3, 19, 8, 10]
new_list = []
for num in listy:
    new_list.append(num + 4)

for i in range(len(listy)):
    listy[i] = listy[i] + 4

listy.sort()

print(listy.index(7))

print(listy)
print(new_list)