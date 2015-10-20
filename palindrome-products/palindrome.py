def is_palindrome(number):
    digits = str(number)
    return all(digits[n] == digits[len(digits) - n - 1] 
               for n in range(len(digits)/2))

def palindrome_list(max_factor, min_factor):
    return [(i * j, (i, j))  
            for i in range(min_factor, max_factor + 1)
            for j in range(min_factor, max_factor + 1)
            if all([i > 0, j >= i, is_palindrome(i * j)])]

def largest_palindrome(max_factor, min_factor=0):
    values, factors = zip(*palindrome_list(max_factor, min_factor))
    return (max(values), factors[values.index(max(values))])
    

def smallest_palindrome(max_factor, min_factor=0):
    values, factors = zip(*palindrome_list(max_factor, min_factor))
    return (min(values), factors[values.index(min(values))])
