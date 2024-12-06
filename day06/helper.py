from utils import insert_in_str_at

# Constants for map symbols
GUARD = '^'
WALL = '#'
PATH = 'X'

X = 0
Y = 1

def	move_guard(input : list, GuardPosition : list, direction : str) -> int:
	x_move = 0
	y_move = 0
	if direction == "NORTH":
		y_move = -1
	elif direction == "EAST":
		x_move = 1
	elif direction == "SOUTH":
		y_move = 1
	elif direction == "WEST":
		x_move = -1
	else:
		return 0
	moves = 0
	while not is_guard_end_of_map(input, GuardPosition)\
		and input[GuardPosition[Y] + y_move][GuardPosition[X] + x_move] != WALL:
		input[GuardPosition[Y]] = insert_in_str_at(GuardPosition[X], input[GuardPosition[Y]], 'X')
		GuardPosition[Y] += y_move
		GuardPosition[X] += x_move
		if not input[GuardPosition[Y]][GuardPosition[X]] == 'X':
			moves += 1
	return moves

def get_guard_position(input : list) -> list:
	for y in range(len(input)):
		for x in range(len(input[y])):
			if input[y][x] == GUARD:
				return [x, y]
	return []

def	is_guard_end_of_map(input : list, GuardPosition : list) -> bool:
	if GuardPosition[Y] == 0 or GuardPosition[X] == 0\
		or (GuardPosition[Y] == len(input) - 1)\
		or (GuardPosition[X] == len(input[0]) - 1):
		return True
	return False
