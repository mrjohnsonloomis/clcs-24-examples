'''
Demonstrates a variety of common while loop structures. 
'''
'''
# Basic While Loop Example
count = 0
while count < 5:
    print(count)
    count += 1

# While Loop with Else Example
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print("Loop completed normally.")
'''
# Infinite While Loop Example
# Uncomment the lines below to run this example.
while True:
     user_input = input("Enter 'exit' to stop: ")
     if user_input == 'exit':
         break

# While Loop with Break and Continue Example
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # Skip 5
    if count == 8:
        break  # Stop at 8
    print(count)
