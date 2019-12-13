# Selection Structures
# Dana Nguyen July 6 2016

# Part 2: Software Sales

# Objective: Calculate the price before and after discount
# ASk for the price of the product
# Ask for the quantity ordered
# Properly label price before and after (if any) discount
# Have the total amount of purchase after the discount

import math

def discount(quantity):
    if quantity < 10:
        percent = 0.00
    elif quantity <= 19:
        percent = 0.10
    elif quantity <= 49:
        percent = 0.20
    elif quantity <=99:
        percent = 0.25
    else:
        percent = 0.30
    return percent

def function(cost, quantity):
    result = cost * quantity * (1 - discount(quantity))
    return result

# funt = function
def subtotal(cost, quantity):
    if quantity < 10:
        result = function(cost, quantity)
    elif quantity <= 19:
        result = function(cost, quantity)
    elif quantity <= 49:
        result = function(cost, quantity)
    elif quantity <= 99:
        result = function(cost, quantity)
    else:
        result = function(cost, quantity)
    return result    

def main():
    print('Discount Availability:', discount(quantity) * 100, '%')
    print('Subtotal: $ ', format(cost * quantity, '.2f'))
    print('Total: $', format(subtotal(cost, quantity), '.2f'))
    print('You saved: $', format(cost * quantity * discount(quantity), '.2f'))

cost = float(input('Enter the price of the product: $ '))
quantity = int(input('Enter the quantity amount: '))

main()
