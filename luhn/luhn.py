class Luhn:
    def __init__(self, number):
        self.number = number
    def convert(self, digit):
        if digit * 2 > 10:
            return digit * 2 - 9
        else:
            return digit * 2
    def addends(self):
        digits = list(int(i) for i in str(self.number)[::-1])
        for n in range(1, len(digits), 2):
           digits[n] = self.convert(digits[n])
        return digits[::-1]
    def checksum(self):
        return sum(self.addends()) % 10
    def is_valid(self):
        return self.checksum() == 0
    @classmethod
    def create(cls, number):
        check_digit = cls(number * 10).checksum()
        if check_digit == 0:
            return number * 10
        else:
            return number * 10 + (10 - check_digit)

