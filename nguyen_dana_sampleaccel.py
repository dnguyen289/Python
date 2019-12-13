# Write a function that has an acceleration and a time
# as its parameters and returns the distnace fallen
# Dana Nguyen June 28 2016

def distance_fallen(accel, time):
    #calculate the result
    #return the result
    distance = 0.5 * accel * (time ** 2)
    result = distance
    return result

earth_d = distance_fallen(9.8, 5)
moon_d = distance_fallen(1.62, 5)

print('Distance fallen on earth:', format(earth_d,'.2f'), 'meters')
print('Distance fallen on moon:', format(moon_d, '.2f'), 'meters')
