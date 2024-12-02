#To convert a list of strings to a list of ints
def list_convert_to_int(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

#Checks if list is increasing
def	is_increasing_list(list):
    for i in range(len(list) - 1):
        is_increasing = list[i] < list[i + 1]
        if not is_increasing:
            return False
    return True

#Checks if list is decreasing
def	is_decreasing_list(list):
    for i in range(len(list) - 1):
        is_decreasing = list[i] > list[i + 1]
        if not is_decreasing:
            return False
    return True

#Checks if list is decreasing
def	has_no_further_distance_than(num, list):
    for i in range(len(list) - 1):
        smaller_than_num = abs(list[i] - list[i + 1]) <= num
        if not smaller_than_num:
            return False
    return True