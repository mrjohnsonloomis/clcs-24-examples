import matplotlib.pyplot as plt

months = []
sales = []

with open('sales_data.txt') as file:
    data = file.readlines()

    for line in data:
        to_parse = line.split(',')
        months.append(to_parse[0])
        sales.append(int(to_parse[1]))

plt.figure(figsize=(10, 5))
plt.plot(months, sales)

plt.show()