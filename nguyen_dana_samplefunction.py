#Determine price of pizza per square unit
#   Not using a function
# Dana Nguyen June 28, 2016

#Find the price per unit of an 8" pizza that costs $6.99

import math

def calc_unit_price(diameter, price):
    area = math.pi * (diameter / 2.0) ** 2
    result = price /area
    return result

def print_results(diameter, per_unit):
    print('Pizza size:', diameter, '-Price per square unit is $'. \
          format(per_unit, '.2f'), sep='')

diameter = 8.0
price = 6.99
area = math.pi * (diameter / 2.0) ** 2
per_unit = price /area
print_results(diameter, per_unit)

diameter2 = 10.0
price2 = 12.99
area2 = math.pi * (diameter2 / 2.0) ** 2
per_unit2 = price2 /area2
print_results(diameter2, per_unit2)

