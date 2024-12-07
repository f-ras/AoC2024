def concatenate_ints(left : int, right : int):
    return int(str(left) + str(right))

def evaluate_equation(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        elif op == '*':
            result *= numbers[i+1]
    return result

def evaluate_equation_pt2(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        elif op == '*':
            result *= numbers[i+1]
        else:
            result = concatenate_ints(result, numbers[i+1])
    return result