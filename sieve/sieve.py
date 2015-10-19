def sieve(number):
    all_numbers = range(2, number+1)
    mark = []
    for i in all_numbers:
        if i not in mark:
            mark += list(j for j in range(2*i, number+1)
                         if j % i == 0)
    return list(n for n in all_numbers if n not in mark)
