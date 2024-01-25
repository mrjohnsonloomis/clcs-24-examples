# Given a 2D list of positive integers
matrix = [
    [10, 23, 56],
    [9, 21, 34],
    [11, 45, 67]
]

# Values to find and limit for replacement
value_to_find = 21
replacement_limit = 20

# Initialize the count, and set min and max to the first element in the matrix
count = 0
min_value = matrix[0][0]
max_value = matrix[0][0]

# Loop through the matrix
for row in matrix:
    for elem in row:
        # Count occurrences of the given value
        if elem == value_to_find:
            count += 1
        # Check for new min or max
        if elem < min_value:
            min_value = elem
        if elem > max_value:
            max_value = elem

# Replace values under the replacement limit
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < replacement_limit:
            matrix[i][j] = -1

# Output results
print(f"The value {value_to_find} occurs {count} times.")
print(f"Minimum value in the matrix is {min_value}.")
print(f"Maximum value in the matrix is {max_value}.")
print("Updated matrix:")
for row in matrix:
    print(row)
