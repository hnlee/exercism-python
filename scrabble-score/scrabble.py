POINTS = dict([(x, 1) for x in 'AEIOULNRST'] +
              [(x, 2) for x in 'DG'] +
              [(x, 3) for x in 'BCMP'] +
              [(x, 4) for x in 'FHVWY'] +
              [(x, 5) for x in 'K'] +
              [(x, 8) for x in 'JX'] + 
              [(x, 10) for x in 'QZ'])

def score(word):
    if any(not x.isalpha() for x in word):
        return 0
    word = word.upper()
    return sum(POINTS[x] for x in word)
