# Falling Object
# Dana Nguyen June 22 2016

# Units for time in seconds
# Enter variables to find distance
# Print, properly labeled distance fallen in units: meters

time = input('Enter the amount of time in seconds: ')

t = float(time)
a = 9.8

distance = 0.5 * a * (t ** 2)
d = format( distance, '7.2f')

print('Distance in meters: ' , d)
