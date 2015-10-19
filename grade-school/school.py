
class School:
    def __init__(self, name):
        self.name = name
        self.db = {}
    def add(self, student, grade_num):
        if grade_num not in self.db:
            self.db[grade_num] = {student}
        else:
            self.db[grade_num] = self.db[grade_num] | {student}
    def grade(self, grade_num):
        if grade_num not in self.db:
            return set()
        else:
            return self.db[grade_num]
    def sort(self):
        return [(i, tuple(sorted(self.db[i]))) for i in self.db]

