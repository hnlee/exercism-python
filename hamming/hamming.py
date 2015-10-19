# Solution to the Hamming exercise


def distance(seq1='', seq2=''):
    return sum(map(lambda x: seq1[x] != seq2[x], range(len(seq1))))
