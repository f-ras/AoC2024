import time
from utils import convert_to_int
from helper import extract_proper_updates
from helper import extract_faulty_updates
from helper import fix_faulty_updates


file = open("input.txt")
input = file.read().splitlines()
file.close()

order_rules = []
updates = []
for line in input:
	if not line:
		continue
	elif line[2] == '|':
		order_rules.append(convert_to_int(line.split('|')))
	else:
		updates.append(convert_to_int(line.split(',')))

faulty_updates_fixed = fix_faulty_updates(extract_faulty_updates(updates, order_rules), order_rules)

result = 0
for update in faulty_updates_fixed:
	result += update[int(len(update) / 2)]

print(result)