# CS020 Midterm - Summer 2016
# Lab Section
# Dana Nguyen

# Objective: Calculate the total price for shipping markers
# Properly label the following: 
# Ask for the number of markers there are
# Account any individual markers and packages
# Print the subtotal
# Show the price of tax and shipping
# Calculate the total at the end and print

marker = int(input('How many markers are you buying? '))
package = marker // 5
separate = marker % 5


package_price = package * 3.5
separate_price = separate * 0.8

subtotal = package_price + separate_price

tax = subtotal * 0.065

shipping = subtotal * 0.05

total = subtotal + tax + shipping


print('Number of packages:', package)
print('Number of separate markers:', separate)

print('Subtotal: $', format(subtotal, '.2f'), sep='')

print('Tax: $', format(tax, '.2f'), sep='')

print('Shipping: $', format(shipping, '.2f'), sep='')

print('Total: $', format(total, '.2f'), sep='')
