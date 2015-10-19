from math import sqrt, ceil

def fermat_method(odd):
    x = ceil(sqrt(odd))
    while x <= odd:
        y = sqrt(x**2 - odd)
        if int(y) == y:
            break
        else:
            x += 1
    return [int(x - y), int(x + y)]

def prime_factors(number):
    factors = []
    while number % 2 == 0:
        factors += [2]
        number = number / 2
    if number != 1:
        tree = [number]
        while len(tree) > 0:
            for n in tree:
                tree.remove(n)
                fermat_factors = fermat_method(n)
                if min(fermat_factors) == 1:
                    factors += [max(fermat_factors)]
                else:
                    tree += fermat_factors    
    return sorted(factors)



