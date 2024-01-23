'''
dictionary.py by M.Johnson

We'll use this program as a starting point to practice using dictionaries.
You'll add your own code to this as you go through the prompted exercises.

'''
#PART A

student_1 = {
    'name': 'Joel Embiid',
    'id_num': '01234',
    'grad_year': 2021 ,
    'courses': ['English', 'Math', 'Science']}

student_2 = {
    'name': 'Tyrese Maxey', 
    'id_num': '01235',
    'grad_year': 2021,
    'courses': ['Spanish', 'Math', 'Art']}

### YOUR CODE GOES BELOW HERE ###
print(student_1['name'])
student_1['name'] = 'James Harden'
print(student_1['name'])

#PART B

students = {'student_1' : {
    'name': 'Joel Embiid',
    'id_num': '01234',
    'grad_year': 2021 ,
    'courses': ['English', 'Math', 'Science']},

    'student_2' : {
    'name': 'Tyrese Maxey',
    'id_num': '01235',
    'grad_year': 2021,
    'courses': ['Spanish', 'Math', 'Art']}
    }

### YOUR CODE GOES BELOW HERE ###
print(students['student_1']['name'])