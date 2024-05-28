def sum_of_digits(x):
    if x < 10:
        return x
    else:
        next = x // 10
        cur = x % 10
        return cur + sum_of_digits(next)

print(sum_of_digits(153))