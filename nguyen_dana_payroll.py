# Selection Structures
# Dana Nguyen July 6 2016

# Part 1: Payroll
# Objective: Calculate the total wage
# Ask user to input the number of hours they worked
# Ask user the hourly rate
# Calculate the total wages for the week
# Output must have $ and 2 decimal places

import math

def wages(hours, rate):
    if hours <= 40:
        result = hours * rate
        print('You have not worked overtime.')
    else: 
        result = 40 * rate + (hours - 40) * rate * 1.5
        print('You have worked overtime.')
    return result

def main():
    print('Your total wage is $', format(wages(hours,rate), '.2f'),
          'for the', hours, 'hours worked, at a $',
          rate, ' per hour rate')

hours = int(input('Enter the number of hours worked: '))
rate = float(input('Enter the hourly rate: '))

main()
