def slices(digit_string, n):
    if n > len(digit_string):
        raise ValueError("Slice is longer than the string.")
    elif n == 0:
        raise ValueError("Zero-length slices are not possible.")
    else:
        return [list(int(j) for j in digit_string[i:i+n]) 
                for i in range(len(digit_string)-n+1)]

def largest_product(digit_string, n):
    if n == 0:
        return 1
    else:
        all_slices = slices(digit_string, n)
        all_products = list(reduce(lambda x, y: x*y, i)
                            for i in all_slices)
        return max(all_products)
