# Importing the necessary library
import matplotlib.pyplot as plt

# Creating data for the line chart
x = list(range(1, 11))  # X-axis values (1 to 10)
y = [xi ** 2 for xi in x]  # Y-axis values (squares of x)

# Creating the line chart
plt.figure(figsize=(10, 5))  # Setting the figure size
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = x^2')  # Plotting the line chart
plt.title('Line Chart: Square Function')  # Adding a title
plt.xlabel('X-axis')  # Adding label for the x-axis
plt.ylabel('Y-axis')  # Adding label for the y-axis
plt.legend()  # Adding a legend
plt.grid(True)  # Adding a grid
plt.show()  # Displaying the chart

# Creating data for the bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 18]

# Creating the bar chart
plt.figure(figsize=(8, 5))  # Setting the figure size
plt.bar(categories, values, color=['red', 'green', 'blue', 'orange', 'purple'])  # Plotting the bar chart
plt.title('Bar Chart: Category Values')  # Adding a title
plt.xlabel('Categories')  # Adding label for the x-axis
plt.ylabel('Values')  # Adding label for the y-axis
plt.show()  # Displaying the chart
