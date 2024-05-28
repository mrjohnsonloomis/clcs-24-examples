def fibonacci(n):
    # Base cases: return 0 if n is 0, and return 1 if n is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: return the sum of the two preceding numbers in the sequence
    else:
        return fibonacci(n-1) + fibonacci(n-2)

