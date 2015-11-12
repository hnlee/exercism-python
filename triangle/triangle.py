class TriangleError(ValueError):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class Triangle(object):
    def __init__(self, *args):
        self.sides = sorted(list(args))
        if len(self.sides) != 3:
            raise TriangleError("Must input three sides.")
        if any(n <= 0 for n in self.sides):
            raise TriangleError("Length must be greater than zero.")
        if self.sides[-1] >= sum(self.sides[:2]):
            raise TriangleError("Violates triangle inequality.")
    def kind(self):
        if len(set(self.sides)) == 1:
            return "equilateral"
        elif len(set(self.sides)) == 2:
            return "isosceles"
        else:
            return "scalene"

