# Variables and Calculations 2
# Dana Nguyen June 22 2016

# Part 2: Minutes of Daylight
# Calculate the amount of sunlight in a day
# Given: The day of year ; The latitude of location
# Print, properly labeled of the number of minutes of sunshine for the day

from math import sin, cos, tan, asin, acos, atan, radians


str_day = input('Enter the amount of days:')
day = int(str_day)


a = tan(0.00860 *(day - 186))
b = 2 * atan(0.9671396 * a)
c = 0.39795 * cos(0.2163108 + b) 

p = asin(c)


str_lat = input('Enter latitude (in degrees):')
latitude = radians(float(str_lat))
lat = float(latitude)


top = sin(0.01454) + sin(lat) * sin(p)
bottom = cos(lat) * cos(p)
frac = top / bottom

d = 7.63944 * acos(frac)
e = 24 - d 

str_re =  e * 60
re = format(str_re, '7.2f')


print('The amount of sunlight in day (in minutes), in the day of your location is:' , re , sep='')

