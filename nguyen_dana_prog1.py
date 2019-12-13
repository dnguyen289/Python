# Dana Nguyen, June 21 2016
# Variables and Calculations 1
# Total Purchase
#To calculate the total price (including 7% tax) up to 5 items

#Input value of items (Currency)
str_item1 = input('Enter price for item 1: $ ')
str_item2 = input('Enter price for item 2: $ ')
str_item3 = input('Enter price for item 3: $ ')
str_item4 = input('Enter price for item 4: $ ')
str_item5 = input('Enter price for item 5: $ ')


#Variables
item1 = float(str_item1)
item2 = float(str_item2)
item3 = float(str_item3)
item4 = float(str_item4)
item5 = float(str_item5)

sub = float(item1 + item2 + item3 + item4 + item5)
tax = sub * 0.07
total = tax + sub

#Calculations
print('Subtotal: $ ' , format(sub , '5.2f') , sep='')
print('Tax: $ ' , format(tax , '5.2f') , sep='')
print('Total: $' , format(total, '5.2f') , sep='')

