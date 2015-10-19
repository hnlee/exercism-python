from math import log10

ENCODE = {'wink': 1,
          'double blink': 10,
          'close your eyes': 100,
          'jump': 1000}
DECODE = dict((log10(ENCODE[x]), x) for x in ENCODE)

def code(shake):
    if any(x not in ENCODE for x in shake):
        return '0'
    binary = sum(ENCODE[x] for x in shake)
    order = [[DECODE[y] for y in sorted(DECODE)].index(x) 
              for x in shake]
    if order[-1] >= order[0]:
        return str(binary)
    else:
        return str(10000 + binary)

def handshake(number):
    try:
        binary = str(bin(number))
    except:
        binary = number
    if 'b' in binary:
        if binary[0] == '-':
            return []
        binary = binary[2:]
    else:
        if any(int(x) > 1 for x in binary):
            return []
    binary = binary.rjust(5, '0')[::-1]
    shake = [DECODE[i] for (i, j) in enumerate(binary[:4]) if j == '1']
    if binary[-1] == '1':
        shake.reverse()
    return shake
