def nth_prime(n):
    primes = [2]
    number = primes[-1]
    while len(primes) < n:
        number += 1
        for i in primes:
            if number % i == 0:
                break
        else:
            primes += [number]
    return primes[-1]
