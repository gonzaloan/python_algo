#
# Given a number of digits N, as well as the sum S of all digits on some password.
# Pass word is the largest number of N digits that can be possible with a given sum s
#
# INPUT
# number of digits and the sum of those digits
# OUTPUT
# the largest number that can be created (or the key) as a list
# SAMPLE INPUT
# sum_of_digits = 20
# number_of_digits = 3
# SAMPLE OUTPUT
# result = [9,9,2]


sum_of_digits = 20
number_of_digits = 3


def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """
    result = []
    current_sum = 0
    for i in range(number_of_digits):
        for num in reversed(range(10)):
            if num + current_sum <= sum_of_digits:
                current_sum += num
                result.append(num)
                break
    if sum(result) != sum_of_digits:
        return [-1]
    return result


print(find_largest_number(number_of_digits, sum_of_digits))
