# Solution to Word Count exercise
# Given a phrase, return a dictionary
# where each key is a word that occurs in the phrase
# and its value is the frequency of that word


def word_count(phrase=''):
    words = phrase.split()
    unique_words = set(words)
    return dict(list((word, words.count(word))
                     for word in unique_words))
