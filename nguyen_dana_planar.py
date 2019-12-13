# Functions
# Dana Nguyen June 30 2016

# Part 2: Distances in Two Dimensions
# Objective: Calculate distance using the Pythagorean formula
# Ask for the x and y coordinates of two points
# Use Pythagorean and city block distance
# Properly label output with 2 decimal places

import math

def distance(x_1, x_2, y_1, y_2):
    x_values = (x_1 - x_2) ** 2
    y_values = (y_1 - y_2) ** 2
    combined = x_values + y_values
    result = (combined) ** (1/2)
    return result


def block_distance(x_1, x_2, y_1, y_2):
    x_values = abs(x_1 - x_2)
    y_values = abs(y_1 - y_2)
    result = x_values + y_values
    return result

def main():
    print('The distance, using Pythagorean formaula, is',
          format(distance(x_1, x_2, y_1, y_2), '.2f'))
    print('The distance, using city-block distance, is',
          format(block_distance(x_1, x_2, y_1, y_2), '.2f'))
    

x_1 = float(input('Enter the x-coordinates of the first point: '))
y_1 = float(input('Enter the y-coordinates of the first point: '))
x_2 = float(input('Enter the x-coordinates of the second point: '))
y_2 = float(input('Enter the y-coordinates of the second point: '))

main()
