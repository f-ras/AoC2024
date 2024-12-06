DEPENDEND = 0
DEPENDEND_ON_THIS = 1

def extract_proper_updates(updates : list, order_rules : list) -> list:
	proper_updates = []
	for update in updates:
		is_proper_update = True
		for i in range(len(update)):
			for j in range(len(order_rules)):
				if update[i] == order_rules[j][DEPENDEND]:
					for check in range(i):
						if update[check] == order_rules[j][DEPENDEND_ON_THIS]:
							is_proper_update = False
		if is_proper_update:
			proper_updates.append(update)
	return proper_updates

def extract_faulty_updates(updates : list, order_rules : list) -> list:
	faulty_updates = []
	for update in updates:
		is_faulty_update = False
		for i in range(len(update)):
			for j in range(len(order_rules)):
				if update[i] == order_rules[j][DEPENDEND]:
					for check in range(i):
						if update[check] == order_rules[j][DEPENDEND_ON_THIS]:
							is_faulty_update = True
		if is_faulty_update:
			faulty_updates.append(update)
	return faulty_updates

def is_faulty_updates(updates : list, order_rules : list) -> bool:
	for update in updates:
		is_faulty_update = False
		for i in range(len(update)):
			for j in range(len(order_rules)):
				if update[i] == order_rules[j][DEPENDEND]:
					for check in range(i):
						if update[check] == order_rules[j][DEPENDEND_ON_THIS]:
							return True
	return False

def fix_faulty_updates(updates : list, order_rules : list) -> list:
	while is_faulty_updates(updates, order_rules):
		for update in updates:
			for i in range(len(update)):
				for j in range(len(order_rules)):
					if update[i] == order_rules[j][DEPENDEND]:
						for check in range(i):
							if update[check] == order_rules[j][DEPENDEND_ON_THIS]:
								temp = update[i]
								update[i] = update[check]
								update[check] = temp
	return updates