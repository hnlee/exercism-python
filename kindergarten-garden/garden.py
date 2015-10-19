
class Garden:
    TYPES = {'G': 'Grass',
             'C': 'Clover',
             'R': 'Radishes',
             'V': 'Violets'}
    CHILDREN = ['Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']
    def __init__(self, layout, students=CHILDREN):
        self.layout = layout.split('\n')
        self.students = sorted(students)
        self.cups = list(self.layout[0][i:i+2] + self.layout[1][i:i+2]
                         for i in range(0, len(self.layout[0]), 2))
    def plants(self, name):
        student_index = self.students.index(name)
        return [self.TYPES[i] for i in self.cups[student_index]]
