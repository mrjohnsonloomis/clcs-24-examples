# Import statements
import math

# Function declarations
def circle_area(radius):
    """Calculate the area of a circle with the given radius."""
    return math.pi * radius ** 2

def greet(name):
    """Print a greeting message to the user."""
    print(f"Hello, {name}!")

# Main script
radius = 5
area = circle_area(radius)
print(f"The area of the circle is: {area}")

name = "Alice"
greet(name)
