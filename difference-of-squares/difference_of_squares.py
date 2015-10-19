def square_of_sum(integer):
    return sum(range(integer+1))**2

def sum_of_squares(integer):
    return sum(map(lambda x: x**2, range(integer+1)))

def difference(integer):
    return square_of_sum(integer) - sum_of_squares(integer)
