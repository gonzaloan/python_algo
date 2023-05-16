#
# Implement a function that returns the minimum number of platforms that are required
# for the train so that none of them waits
# INPUT
# Two lists represent arrival and departure times of trains that stop
# OUTPUT
# Minimum number of platforms required
# SAMPLE INPUT
# arrival= [900,940,950,1100, 1500, 1800]
# departure=[910, 1200, 1120, 1130, 1900, 2000]
# SAMPLE OUTPUT
# result = 3 # BC at 11:00 there will be 3 trains there.
#
#

def find_platform(arrival, departure):
    result = 0
    minimum_number = 1
    last_train = departure[0]
    idx = 1
    while idx < len(arrival):
        if departure[idx] < last_train:
            minimum_number += 1
        else:
            if minimum_number > result:
                result = minimum_number
            minimum_number = 1
            last_train = departure[idx]
        idx += 1
    return result


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

print(find_platform(arrival, departure))
