from math import sqrt

def is_triplet(triplet):
    [a, b, c] = sorted(triplet)
    return a**2 + b**2 == c**2

def triplets_in_range(minimum, maximum):
    ab = set((a, b) for a in range(minimum, maximum+1)
             for b in range(minimum, maximum+1)
             if a != b and a**2 + b**2 <= maximum**2)
    abc = ((min([a, b]), max([a, b]), int(sqrt(a**2 + b**2))) 
           for (a, b) in ab)
    return set((a, b, c) for (a, b, c) in abc
               if is_triplet((a, b, c)))

def is_coprime(x, y):
    x_divisors = set(z for z in range(1, x+1) if x % z == 0)
    y_divisors = set(z for z in range(1, y+1) if y % z == 0) 
    return x_divisors & y_divisors == {1}

def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError('Argument must be an integer divisible by 4')
    mn = ((m, n) for m in range(1, b/2+1) for n in range(1, b/2+1) 
          if m > n and m*n == b/2)
    abc = ((min(m**2 - n**2, b), max(m**2 - n**2, b), m**2 + n**2) 
           for (m, n) in mn
           if (m - n) % 2 == 1 and is_coprime(m, n))
    return set((a, b, c) for (a, b, c) in abc if is_triplet((a, b, c)))
