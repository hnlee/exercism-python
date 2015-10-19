class Matrix:
    def __init__(self, matrix):
        self.rows = [[int(number) for number in row.split()]
                     for row in matrix.split('\n')]
        self.columns = [list(column) for column in zip(*self.rows)]
