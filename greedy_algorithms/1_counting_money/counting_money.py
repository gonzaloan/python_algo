#
#Given an infinite number of quarters (25cents),dimes (10cents), nickels(5cents) and pennies(1cent)
#implement a function to calculate the minimum number of coins to represent v cents
#
# INPUT:
#  v: total money to convert to coins and a list of available coins.
# OUTPUT:
#  the minimum number of coins among the available coins that add up to the original number v, i.e. the coins
# represent v cents
#
# Sample INPUT
#  v = 19
# available_coins = [1,5,10,25]
#
# Sample OUTPUT
# result = [10, 5, 1,1, 1, 1 ]


def find_min_coins(v, coins_available):
    result = []
    current = 0
    index = len(coins_available) - 1
    while index != -1:
        actual = current + coins_available[index]
        if coins_available[index] <= v and actual <= v:
            result.append(coins_available[index])
            current = actual
        else:
            index -= 1
    return result


v = 19
available_coins = [1,5,10,25]
print(find_min_coins(v, available_coins))

