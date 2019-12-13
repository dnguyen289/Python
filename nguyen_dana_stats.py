# Functions
# Dana Nguyen June 30 2016

# Part 1: Statistical Functions
# Objective: Calculate the reciprocal and the means
# Means = Arithmetic, Geometric, Harmonic

import math

def reciprocal(n):
    result = 1 / n
    return result

def mean(x, y, z):
    result = (x + y + z) / 3
    return result

def geometric_mean(x, y, z):
    result = (x * y * z) ** (1/3)
    return result

def harmonic_mean(x, y, z):
    bottom = reciprocal(x) + reciprocal(y) + reciprocal(z)
    result = 3 / bottom
    return result


def main():
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")

    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")

    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
        "[should be 12.0]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8), \
        "[should be 8.4]")
  
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
        "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
        "[should be 2.0]")

main()
