def max(list):
    if len(list) == 1:
        return list[0]
    else:
        cur = list[0]
        next = max(list[1:])
        if cur > next:
            return cur
        else: 
            return next

print(max([2, 9, 3]))