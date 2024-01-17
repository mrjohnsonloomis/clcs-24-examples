'''
Demonstrates how list comprehensions work.
'''
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

# Create a list of all the scores that are greater than or equal to 90
# using a list comprehension
high_scores = [score for score in test_scores if score >= 90]
print(high_scores)


