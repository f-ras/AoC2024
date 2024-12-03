
#Extract mul instructions
def	extract_uncorrupted_mul_instructions(input) -> list:
	uncorrupted_mul_instructions = []
	for index in range(len(input)):
		if input[index:index+4] == "mul(":
			start_location = index
			index += 4
		else:
			continue
		if not input[index:index+1].isdigit():
			continue
		while input[index:index+1].isdigit():
			index += 1
		if input[index] == ',':
			index += 1
		else:
			continue
		if not input[index:index+1].isdigit():
			continue
		while input[index:index+1].isdigit():
			index += 1
		if input[index] == ')':
			index += 1
			uncorrupted_mul_instructions.append(input[start_location:index])
	return uncorrupted_mul_instructions

#Extract all instructions (mul, do and don't)
def	extract_uncorrupted_instructions_complete(input) -> list:
	uncorrupted_instructions = []
	for index in range(len(input)):
		if input[index:index+4] == "mul(":
			start_location = index
			index += 4
		elif input[index:index+4] == "do()":
			start_location = index
			index += 4
			uncorrupted_instructions.append(input[start_location:index])
			continue
		elif input[index:index+7] == "don't()":
			start_location = index
			index += 7
			uncorrupted_instructions.append(input[start_location:index])
			continue
		else:
			continue
		if not input[index:index+1].isdigit():
			continue
		while input[index:index+1].isdigit():
			index += 1
		if input[index] == ',':
			index += 1
		else:
			continue
		if not input[index:index+1].isdigit():
			continue
		while input[index:index+1].isdigit():
			index += 1
		if input[index] == ')':
			index += 1
			uncorrupted_instructions.append(input[start_location:index])
	return uncorrupted_instructions