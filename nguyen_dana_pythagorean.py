# Pythagorean Theorem program
# Asks for lengths of side a and b of a right triangle
# calculates hypo c, proplerly labeled
# Dana Nguyen June 22 2016

# Ask for side a
# Ask for side b
# Calculate c as square root of (side a squared plus side b squared).
# print results, properly labeled

str_a = input('Enter length of side a of the right triangle: ')
str_b = input('Enter length of side b of the right triangle: ')

a = float(str_a)
b = float(str_b)

from math import sqrt

c = sqrt(a**2 + b**2)

print('C = ' , c , sep='')

