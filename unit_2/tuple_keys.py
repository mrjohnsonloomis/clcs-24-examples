# Create a dictionary with tuple keys
student_grades = {('John', 'Doe'): 'A', ('Jane', 'Doe'): 'B'}

# Access a value using a tuple key
print(student_grades[('John', 'Doe')])

# Adding a new entry using a tuple as the key
student_grades[('Emily', 'Clark')] = 'A+'

# You can still access the elements of the tuple
for key in student_grades:
    fname, lname = key
    print(fname)

# Display the updated dictionary
print(student_grades)
