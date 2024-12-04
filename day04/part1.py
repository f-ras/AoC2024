file = open("input.txt")
input = file.read().splitlines()
file.close()

line_length = len(input[0])

xmas_found = 0
# Check 1: Horizontal
# Check 2: Horizontal (backwards)
# Check 3: Vertical
# Check 4: Vertical (backwards)
# Check 5: Diagonal right-left
# Check 6: Diagonal right-left (backwards)
# Check 7: Diagonal left-right
# Check 8: Diagonal left-right (backwards)
for lineID in range(len(input)):
	for charID in range(len(input[lineID])):
		if input[lineID][charID:charID+4] == "XMAS":
			xmas_found += 1
		if input[lineID][charID:charID+4] == "SAMX":
			xmas_found += 1
		if lineID >= 3 and \
			input[lineID - 3][charID] == "X" and input[lineID - 2][charID] == "M" and\
			input[lineID - 1][charID] == "A" and input[lineID - 0][charID] == "S":
			xmas_found += 1
		if lineID >= 3 and \
			input[lineID - 3][charID] == "S" and input[lineID - 2][charID] == "A" and\
			input[lineID - 1][charID] == "M" and input[lineID - 0][charID] == "X":
			xmas_found += 1
		if lineID >= 3 and charID >= 3 and\
			input[lineID - 3][charID - 3] == "S" and input[lineID - 2][charID - 2] == "A" and\
			input[lineID - 1][charID - 1] == "M" and input[lineID - 0][charID - 0] == "X":
			xmas_found += 1
		if lineID >= 3 and charID >= 3 and\
			input[lineID - 3][charID - 3] == "X" and input[lineID - 2][charID - 2] == "M" and\
			input[lineID - 1][charID - 1] == "A" and input[lineID - 0][charID - 0] == "S":
			xmas_found += 1
		if lineID >= 3 and (line_length - charID) >= 4 and\
			input[lineID - 3][charID + 3] == "S" and input[lineID - 2][charID + 2] == "A" and\
			input[lineID - 1][charID + 1] == "M" and input[lineID - 0][charID + 0] == "X":
			xmas_found += 1
		if lineID >= 3 and (line_length - charID) >= 4 and\
			input[lineID - 3][charID + 3] == "X" and input[lineID - 2][charID + 2] == "M" and\
			input[lineID - 1][charID + 1] == "A" and input[lineID - 0][charID + 0] == "S":
			xmas_found += 1

print(xmas_found)