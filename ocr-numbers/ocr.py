FONT = [[" _ ", "| |", "|_|"],
        ["   ", "  |", "  |"],
        [" _ ", " _|", "|_ "],
        [" _ ", " _|", " _|"],
        ["   ", "|_|", "  |"],
        [" _ ", "|_ ", " _|"],
        [" _ ", "|_ ", "|_|"],
        [" _ ", "  |", "  |"],
        [" _ ", "|_|", "|_|"],
        [" _ ", "|_|", " _|"]]


def number(digits):
    if len(digits) != 4 or any(len(row) % 3 != 0 for row in digits):
        raise ValueError
    if digits[-1] != ' ' * len(digits[0]) or \
       any(not set(row).issubset(set(" _|")) for row in digits):
        return '?'
    columns = zip(*digits[:-1])
    triplets = [[''.join(j) for j in zip(*columns[i:i+3])]
                for i in range(0, len(columns), 3)]
    return ''.join(str(FONT.index(i)) if i in FONT else '?'
                   for i in triplets)

def grid(digits):
    if not digits.isdigit():
        raise ValueError
    triplets = [FONT[int(i)] for i in digits]
    rows = [''.join(i) for i in zip(*triplets)]
    return rows + [' ' * len(rows[0])]
