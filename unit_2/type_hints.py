# demonstrates how to use type hints

def add(x:int, y:int)->int:
    print(f"Adding {x} and {y}...")
    return (x + y)

def greater(x:int, y:int)->bool:
    if x > y:
        return True
    else:
        return False

def average(x:float, y:float)->float:
    return (x + y) / 2

print(add(2.5, 3))