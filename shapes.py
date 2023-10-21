print()
import math

# Circle
r = float(input('Enter the radius of the circle  '))
print(f'The area of the circle with the radius {r:.2f} is: {math.pi*r:.2f}')

# Triangle
a = float(input('Enter the base of the triangle  '))
h = float(input ('Enter the hight of the triangle  '))
print(f'The area of the triangle with the base {a:.2f} and with the hight {h:.2f} is: {a*h/2:.2f}')

# Rectangle
l = float(input('Enter the length of the rectangle  '))
w = float(input('Enter the width of the rectangle  '))
print(f'The area of the rectangle with the length {l:.2f} and with the width {w:.2f} is: {l*w:.2f}')

def rectangle_area(side1, side2):
    return side1*side2

def triangle_area(base, height):
    return base*height/2

def circle_area(radius):
    return math.pi*radius**2

def square_perimeter(length):
    return length*4

def circle_details(radius):
    circumference = math.pi*radius
    area = math.pi*radius**2
    return circumference, area

def geometry (length, radius):
    square_area = length**2
    square_perimeter = length * 4
    circle_area = math.pi * radius**2
    circle_curcumference = 2 * math.pi * radius
    values = [square_area, circle_area, square_perimeter, circle_curcumference]

    return values

print(f'{"Square" if geometry(5, 3)[0] > geometry(5, 3)[1] else "Circle"} has a larger area')
print(f'{"Square has a larger perimeter" if geometry(5, 3)[2] > geometry(5, 3)[3] else "Circle has a larger curcumference"}')