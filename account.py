# Final Project
# Dana Nguyen July 27 2016

# The Bank Account Class
# Objective: Have the follwing attributes:
#   acct_number: the account number (an integer)
#   name: the account holder’s name
#   pin: the account holder’s PIN, which is a four-character string,
#       since it can have leading zeros.
#   balance: the current balance in the account, which is a float.

class Account:

def __init__(self, acct_number, name, pin, balance):
    acct_number = int(acct_number)
    name = str(name)
    pin = str(pin)
    balance = float(balance)

def __str__(self):
    
def deposit(self, amount)
    self.money += amount
    return self.money

def withdraw(self, amount)
    self.money -= amount
    return self.money
