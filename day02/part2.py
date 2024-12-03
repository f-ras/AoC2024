from utils import list_convert_to_int
from utils import is_increasing_list
from utils import is_decreasing_list
from utils import has_no_further_distance_than

# Define function to wrap all checks for safe report
def is_safe(report):
    return (is_decreasing_list(report) or is_increasing_list(report)) \
            and has_no_further_distance_than(3, report)

# Get input
file = open("input.txt")
input = file.read().splitlines()
file.close()

# Empty list for appending
unsafe_reports = []

# Check everything as is - saving unsafe_reports
safe_reports = 0
for line in input:
    report = list_convert_to_int(line.split())
    if is_safe(report):
        safe_reports += 1
    else:
        unsafe_reports.append(report)

# Double check with single removals, checking this from temporary lists
for report in unsafe_reports:
    for i in range(len(report)):
        temp = report.copy()
        temp.pop(i)
        if is_safe(temp):
            safe_reports += 1
            break

print(f"Total safe reports: {safe_reports}")