from extractions import extract_uncorrupted_instructions_complete

#Open files
file = open("input.txt")
input = file.read()
file.close()

#Create lists
uncorrupted_instructions = extract_uncorrupted_instructions_complete(input)
multiplies_to_execute = []

#Filter out only mul-instructions after do()
do = True
for index in range(len(uncorrupted_instructions)):
	if uncorrupted_instructions[index] == "don't()":
		do = False
		continue
	if uncorrupted_instructions[index] == "do()":
		do = True
		continue
	if do == True:
		multiplies_to_execute.append(uncorrupted_instructions[index])

#Multiply all do() instructions
result = 0
for instruction in multiplies_to_execute:
	value = instruction.strip("mul()").split(',')
	value[0] = int(value[0])
	value[1] = int(value[1])
	result += value[0] * value[1]

print(result)

