'''
Demonstrates the effective use of ternary operators.
'''

def greeting(name:str, time:int)->str:
    return f"Good morning {name}!" if time < 12 else f"Good afternoon {name}!" 

def class_length(day:str)->int:
    return 50 if day == 'Wednesday' else 75