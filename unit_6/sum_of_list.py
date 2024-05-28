def sum_list(listy):
    # Base case: if the array is empty, return 0
    if len(listy) == 0:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the array
    else:
        return listy[0] + sum_list(listy[1:])
    
print(sum_list([5,4,5]))
