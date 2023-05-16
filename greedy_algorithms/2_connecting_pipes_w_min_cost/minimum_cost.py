# Implement a function that connects n pipes of different lengths, into one pipe.
# You can assume that the cost to connect two pipes is equal to the sum of their lengths.
# We need to connect the pipes with minimum cost.
#
# INPUT
# a list oc containing lengths of n pipes
# OUTPUT
# the total cost of connecting the pipes
# SAMPLE INPUT
# pipes = [4,3,2,6]
# SAMPLE OUTPUT
# result = 29

def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """
    pipes.sort()
    idx = 0
    if idx + 1 > len(pipes):
        return pipes[0]

    actual = pipes[idx] + pipes[idx +1]
    idx += 2
    cost = actual
    while idx < len(pipes):
        print('idx: ', idx)
        actual += pipes[idx]
        cost = cost + actual
        idx += 1
    return cost


pipes = [4, 3, 2, 6]
print(min_cost(pipes))
