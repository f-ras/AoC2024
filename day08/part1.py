# Read input from file
with open("input.txt") as file:
    input = file.read().splitlines()

coordinates = []
for ascii_value in range(0, 127):
    coordinates.append([])



print(coordinates[ord('A')])

for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] != '.':
            antenna_value = input[y][x]
            coordinates[ord(antenna_value)].append([x, y])

print(coordinates[ord('A')])
