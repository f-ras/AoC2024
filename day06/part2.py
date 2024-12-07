from helper import get_guard_position
from helper import is_guard_end_of_map
from helper import move_guard_pt2
from utils import insert_in_str_at
import copy

# Constants for map symbols
GUARD = '^'
WALL = '#'
PATH = 'X'
REPEATING_PATH = 'O'

X = 0
Y = 1
# Read input from file
with open("input.txt") as file:
    input = file.read().splitlines()

import time
# Move the guard until it reaches the end of the map
def is_guard_running_around_in_loops(input : list) -> bool:
	directions = ["NORTH", "EAST", "SOUTH", "WEST"]
	path_repeats = 0
	while not is_guard_end_of_map(input, GuardPosition):
		for direction in directions:
			move_guard_pt2(input, GuardPosition, direction)
			if input[GuardPosition[Y]][GuardPosition[X]] == REPEATING_PATH:
				path_repeats += 1
			# print(f"repeat{path_repeats}")
			# time.sleep(1)
			if path_repeats == 4:
				return True
	return False

import time
loops = 0
for y in range(len(input)):
	for x in range(len(input[y])):
		GuardPosition = get_guard_position(input)
		if GuardPosition[X] == x and GuardPosition[Y] == y:
			continue
		temp = input.copy()
		temp[y] = insert_in_str_at(x, temp[y], WALL)
		loops += is_guard_running_around_in_loops(temp)
		for line in temp:
			print(line)
		print(loops)
		print('\n')
		# time.sleep(0.1)

print(f"Final position {GuardPosition}")
# print(loops)