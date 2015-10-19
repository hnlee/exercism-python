# Solution to RNA Transcription exercise
# Given DNA sequence, return RNA complement


def to_rna(dna=''):
    COMPLEMENT = {'A': 'U',
                  'T': 'A',
                  'C': 'G',
                  'G': 'C'}
    return ''.join(list(COMPLEMENT[base] for base in dna))
