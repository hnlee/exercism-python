class Phone:
    INVALID = '0' * 10
    def __init__(self, number):
        digits = ''.join(n for n in number if n.isdigit())
        if len(digits) < 10 or len(digits) > 11:
            self.number = self.INVALID
        elif len(digits) == 11:
            if digits[0] == '1':
                self.number = digits[1:]
            else:
                self.number = self.INVALID
        else:
            self.number = digits
    def pretty(self):
        return "({0}) {1}-{2}".format(self.number[:3],
                                      self.number[3:6],
                                      self.number[6:])
    def area_code(self):
        return self.number[:3]
