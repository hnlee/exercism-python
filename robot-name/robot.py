from random import choice, randint, seed
from string import ascii_uppercase

class Robot:
    def generate_name(self):
        seed()
        return ''.join([choice(ascii_uppercase) for i in range(2)] +
                       [str(randint(0, 9)) for i in range(3)])

    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        self.name = self.generate_name() 


