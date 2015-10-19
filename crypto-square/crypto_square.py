from string import whitespace, punctuation
from math import sqrt, ceil

def encode(message):
    if not message:
        return ''
    message = message.lower().translate(None, whitespace + punctuation)
    col = int(ceil(sqrt(len(message))))
    rectangle = [message[i:i+col] 
                 for i in range(0, len(message), col)]
    rectangle[-1] = rectangle[-1].ljust(col)
    transpose = (reduce(lambda x, y: x + y, z).replace(' ', '')
                 for z in zip(*rectangle))
    return ' '.join(transpose)
