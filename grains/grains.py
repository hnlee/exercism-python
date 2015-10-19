def on_square(number):
    return 2**(number-1)

def total_after(number):
    return reduce(lambda x, y: x + y, list(2**i for i in range(number)))
