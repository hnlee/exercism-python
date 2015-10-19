def parse_binary(number):
    if any(x not in ("0", "1") for x in number):
        raise ValueError("Input is not a binary number.")
    number = number[::-1]
    return sum(2**i * int(j) for (i, j) in enumerate(number))
