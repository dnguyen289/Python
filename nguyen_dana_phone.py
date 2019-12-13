# Selection Structures
# Dana Nguyen July 6 2016

# Part 3: Phone Plan
# Plan 1: $9.38 plus 4.5 cents for each unit used over 65 units.
# Plan 2: $8.57 plus 5.2 cents for each unit used over 50 units.
# Objective: Tell whether phone plan 1 or 2 is cheaper
# Ask the user for number of units used
# Calculate and display the cost for the units
#   using the first plan or second plan.
# Tell which plan is cheaper.

import math

def plan1(units):
    if units < 0:
        result = print('You cannot have negative units')
    elif units > 65:
        result = 9.38 + ( 0.045 * (units - 65))
        return result
    else:
        result = 9.38
        return result

def plan2(units):
    if units < 0:
        result = print('You cannot have negative units')
    elif units > 50:
        result = 8.57 + ( 0.052 * (units - 50))
        return result
    else:
        result = 8.57
        return result


def comparison(plan_1, plan_2):
    plan_1 = plan1(units)
    plan_2 = plan2(units)
    if plan_1 > plan_2:
        result = print('Plan 2 is cheaper')
    elif plan_2 > plan_1:
        result = print('Plan 1 is cheaper')
    return result

units = int(input('Enter number of units used: '))

def main():
    print('Cost for plan 1: $', format(plan1(units), '.2f'))
    print('Cost for plan 2: $', format(plan2(units), '.2f'))
    comparison(plan1, plan2)

main()

