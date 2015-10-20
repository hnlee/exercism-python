HEX_DEC = dict(zip([str(n) for n in range(10)] + 
                   [n for n in 'ABCDEF'],
                   range(16)))

def hexa(hexastring):
    if any(n.upper() not in HEX_DEC for n in hexastring):
        raise ValueError
    return sum(HEX_DEC[j.upper()] * (16**i) 
               for i, j in enumerate(hexastring[::-1]))
