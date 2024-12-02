from utils import list_convert_to_int
from utils import is_increasing_list
from utils import is_decreasing_list
from utils import has_no_further_distance_than

file = open("input.txt")
input = file.read().splitlines()
file.close()

safe_reports = 0
for line in input:
    report = list_convert_to_int(line.split())
    if (is_decreasing_list(report) or is_increasing_list(report)) \
        and has_no_further_distance_than(3, report):
        safe_reports += 1

print(f"Total safe reports: {safe_reports}")