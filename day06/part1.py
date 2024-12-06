from helper import get_guard_position
from helper import is_guard_end_of_map
from helper import move_guard


# Read input from file
with open("input.txt") as file:
    input = file.read().splitlines()

# Find the guard's starting position
GuardPosition = get_guard_position(input)

moves = 1
directions = ["NORTH", "EAST", "SOUTH", "WEST"]

# Move the guard until it reaches the end of the map
while not is_guard_end_of_map(input, GuardPosition):
	for direction in directions:
		moves += move_guard(input, GuardPosition, direction)

print(f"Final position {GuardPosition}")
for line in input:
	print(line)
print(moves)