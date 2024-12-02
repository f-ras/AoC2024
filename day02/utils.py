#To convert a list of strings to a list of ints
def convert_list_to_int(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

#Checks if list is increasing
def	list_is_increasing(list):
    for i in range(len(list) - 1):
        is_increasing = list[i] < list[i + 1]
        if not is_increasing:
            return False
    return True

#Checks if list is decreasing
def	list_is_decreasing(list):
    for i in range(len(list) - 1):
        is_decreasing = list[i] > list[i + 1]
        if not is_decreasing:
            return False
    return True

#Checks if list is decreasing
def	list_has_no_further_distance_than(num, list):
    for i in range(len(list) - 1):
        smaller_than_num = abs(list[i] - list[i + 1]) <= num
        if not smaller_than_num:
            return False
    return True