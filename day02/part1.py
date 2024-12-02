from utils import convert_list_to_int
from utils import list_is_increasing
from utils import list_is_decreasing
from utils import list_has_no_further_distance_than

file = open("input.txt")
input = file.read().splitlines()
file.close()

safe_reports = 0
for line in input:
    report = convert_list_to_int(line.split())
    if (list_is_decreasing(report) or list_is_increasing(report)) \
        and list_has_no_further_distance_than(3, report):
        safe_reports += 1

print(f"Total safe reports: {safe_reports}")