import re
from operator import add, sub, mul, div

OPERATIONS = {"plus": add, 
              "minus": sub, 
              "multiplied by": mul, 
              "divided by": div}

def calculate(problem):
    form = re.compile("What is ([\-\w ]+)?")
    parts = re.match(form, problem)
    if parts is None:
        raise ValueError
    numbers = re.findall(re.compile("[\-\d]+"), parts.group(1))
    operators = re.findall(re.compile("plus|minus|multiplied by|divided by"),
                           parts.group(1))
    if len(numbers) != len(operators) + 1:
        raise ValueError
    answer = int(numbers[0])
    for i, j in enumerate(operators):
        answer = OPERATIONS[j](answer, int(numbers[i + 1]))
    return answer
    
