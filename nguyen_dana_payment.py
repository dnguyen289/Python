# Variables and Calculations 2
# Dana Nguyen June 22 2016

# Part 1: Monthly interest Rate Calculator
# Calculate monthly payments on a loan

# Variables: p = initial amount
# Variables: r = monthly interest rate
# Variables: n = number of months
# Print, properly labeled the monthly payment ( m )

from math import pow

inital = input('Enter the initial amount on a loan: $' )
rate = input('Enter the monthly interest rate (in decimal form): ' )
months = input ('Enter the number of months of the loan: ' )

p = float(inital)
r = float(rate)
n = int(months)

top =  r * pow(1+r , n)
bottom = pow (1+r, n) - 1
fraction = top / bottom

payment = p * fraction

m = format(payment , '7.2f')

print('Monthly payment: $' , m )


