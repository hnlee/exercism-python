from string import ascii_lowercase, whitespace, punctuation, digits,maketrans
from random import choice

class Caesar:
    NONLETTERS = whitespace + punctuation + digits
    KEY = ascii_lowercase[3:] + ascii_lowercase[:3]
    def encode(self, message):
        shift = maketrans(ascii_lowercase, self.KEY)
        return message.lower().translate(shift, self.NONLETTERS) 
    def decode(self, message):
        deshift = maketrans(self.KEY, ascii_lowercase)
        return message.lower().translate(deshift, self.NONLETTERS)

class Cipher:
    LETTERS = ascii_lowercase * 2
    def __init__(self, key=''):
        if not key:
            self.key = reduce(lambda x, y: x + y, 
                              (choice(ascii_lowercase) 
                               for n in range(100)))
        elif not key.islower():
            raise ValueError('Key must be all in lowercase.')
        elif not key.isalpha():
            raise ValueError('Key must be all alphabetic characters.')
        else:
            self.key = key
    def encode(self, message):
        if len(self.key) != len(message):
            if len(self.key) < len(message):
                self.key = self.key * (len(message) / len(self.key)) + \
                           self.key[:len(message) % len(self.key)] 
            else:
                self.key = self.key[:len(message)]
        shift = (self.LETTERS.index(n) for n in self.key)
        indices = (self.LETTERS.index(n) for n in message.lower())
        return reduce(lambda x, y: x + y,
                      map(lambda i, j: self.LETTERS[i + j],
                          shift, indices))
    def decode(self, message):
        if len(self.key) != len(message):
            if len(self.key) < len(message):
                self.key = self.key * (len(message) / len(self.key)) + \
                           self.key[:len(message) % len(self.key)] 
            else:
                self.key = self.key[:len(message)]
        deshift = (self.LETTERS.index(n) for n in self.key)
        indices = (self.LETTERS.index(n) for n in message.lower())
        return reduce(lambda x, y: x + y,
                      map(lambda i, j: self.LETTERS[j - i],
                          deshift, indices))


