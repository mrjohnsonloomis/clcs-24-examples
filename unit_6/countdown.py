def countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)
        print(f'returning {n}')

countdown(10)

'''
STACK
10 countdown(9)
9 countdown(8)
8 countdown(7)
7 countdown(6)
6 countdown(5)
5 countdown(4) 
4 countdown(3)
3 countdown(2)
2 countdown(1)
1 countdown(0)
BLASTOFF! --> return (BASE CASE)

'''

