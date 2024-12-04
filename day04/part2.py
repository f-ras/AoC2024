file = open("input.txt")
input = file.read().splitlines()
file.close()

xmas_found = 0
# Check 1: M-left
# Check 2: M-right
# Check 3: M-top
# Check 4: M-bottom
for lineID in range(len(input)):
	for charID in range(len(input[lineID])):
		if lineID < 2:
			break
		if charID < 2:
			continue
		if input[lineID - 2][charID - 2] == "M" and input[lineID - 2][charID] == "S" and \
						input[lineID - 1][charID - 1] == "A" and\
			input[lineID][charID - 2] == "M" and input[lineID][charID] == "S":
			xmas_found += 1
		if input[lineID - 2][charID - 2] == "S" and input[lineID - 2][charID] == "M" and \
						input[lineID - 1][charID - 1] == "A" and\
			input[lineID][charID - 2] == "S" and input[lineID][charID] == "M":
			xmas_found += 1
		if input[lineID - 2][charID - 2] == "M" and input[lineID - 2][charID] == "M" and \
						input[lineID - 1][charID - 1] == "A" and\
			input[lineID][charID - 2] == "S" and input[lineID][charID] == "S":
			xmas_found += 1
		if input[lineID - 2][charID - 2] == "S" and input[lineID - 2][charID] == "S" and \
						input[lineID - 1][charID - 1] == "A" and\
			input[lineID][charID - 2] == "M" and input[lineID][charID] == "M":
			xmas_found += 1

print(xmas_found)