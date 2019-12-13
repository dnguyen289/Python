# Functions
# Dana Nguyen June 30 2016

# Part 3: Spherical Distance
# Objective: Calculate the distance between two cities on Earth
# Calculates the distance of the following:
#   San Jose to Chicago
#   Chicago to Washington D.C.
# Properly label and print the distances (miles and kilometers) [as integers]

from math import cos, sin, acos, radians

def great_circle_distance(lat_1, lat_2, long_1, long_2):
    r_lat_1 = radians(lat_1)
    r_lat_2 = radians(lat_2)
    r_long_1 = radians(long_1)
    r_long_2 = radians(long_2)
    a = abs(r_long_1 - r_long_2)
    angle = acos(sin(r_lat_1) * sin(r_lat_2) + cos(r_lat_1) * cos (r_lat_2) * cos(a))
    r = 6371
    result = r * angle
    return result

def km_to_miles(lat_1, lat_2, long_1, long_2):
    result = great_circle_distance(lat_1, lat_2, long_1, long_2) * 0.621371
    return result

# miles = km_to_miles(lat_1, lat_2, long_1, long_2)

def main():
    print('The distance between San Jose to Chicago is',
          int(great_circle_distance(37.33, 41.83, -121.9, -87.68)),
          'kilometers, or',
          int(km_to_miles(37.33, 41.83, -121.9, -87.68)),
          'miles')
    print('The distance between Chicago to Washington D.C. is',
          int(great_circle_distance(41.83, 38.90, -87.68, -77.02)),
          'kilometers, or',
          int(km_to_miles(41.83, 38.90, -87.68, -77.02)),
          'miles')


main()

