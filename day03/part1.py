from extractions import extract_mul_uncorrupted_instructions

file = open("input.txt")
input = file.read()
file.close()

uncorrupted_mul_instructions = extract_mul_uncorrupted_instructions(input)
result = 0
for instruction in uncorrupted_mul_instructions:
	value = instruction.strip("mul()").split(',')
	value[0] = int(value[0])
	value[1] = int(value[1])
	result += value[0] * value[1]

print(result)