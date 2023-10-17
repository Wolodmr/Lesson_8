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


