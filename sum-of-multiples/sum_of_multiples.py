def sum_of_multiples(number, factors=[3, 5]):
    multiples = list(range(i, number, i) for i in factors
                     if i != 0)
    if not multiples:
        return 0
    else:
        return sum(set(reduce(lambda x, y: x + y, multiples)))
