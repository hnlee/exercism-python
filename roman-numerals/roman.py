def numeral(arabic):
    roman = ''
    numerals = {1000: 'M', 
                500: 'D', 
                100: 'C', 
                50: 'L', 
                10: 'X', 
                5: 'V', 
                1: 'I'}
    order = sorted(numerals, reverse=True)
    for i, j in enumerate(order):
        if i % 2 == 0:
            if arabic/j == 4:
                roman += numerals[j] + numerals[order[i-1]]
            else:
                roman += numerals[j] * (arabic/j)
            arabic = arabic % j
        elif arabic/j > 0:
            if arabic/order[i+1] == 9:
                roman += numerals[order[i+1]] + numerals[order[i-1]]
                arabic = arabic % order[i+1]
            else:
                roman += numerals[j]
                arabic = arabic % j
        else:
            continue
    return roman
