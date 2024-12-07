import itertools

from utils import convert_to_int
from helper import evaluate_equation

# Read input from file
with open("input.txt") as file:
    input = file.read().splitlines()

#Extract equations and convert to ints
equation_result = []
numbers = []
for line in input:
    line = line.replace(":", "").split(' ')
    equation_result.append(int(line[0]))
    numbers.append(convert_to_int(line[1:]))

#Find solutions
found_solutions = 0
for index in range(len(numbers)):
    num_gaps = len(numbers[index]) - 1
    operator_cobinations = itertools.product(['+', '*'], repeat=num_gaps)
    for operators in operator_cobinations:
        if evaluate_equation(numbers[index], operators) == equation_result[index]:
            found_solutions += evaluate_equation(numbers[index], operators)
            break

print(found_solutions)