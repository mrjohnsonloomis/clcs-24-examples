import matplotlib.pyplot as plt

months = []
sales_1 = []
sales_2 = []

with open('sales_data_2.txt') as file:
    data = file.readlines()

    for line in data:
        to_parse = line.split(',')
        months.append(to_parse[0])
        sales_1.append(int(to_parse[1]))
        sales_2.append(int(to_parse[2]))


plt.plot(months, sales_1, label='Last Year')
plt.plot(months, sales_2, label='This year')

plt.title('Sales Last Year vs This Year')
plt.xlabel('Months in Year')
plt.ylabel('Millions Units Sold')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()