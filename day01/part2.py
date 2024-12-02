file = open("input.txt")
input = file.read().split()
file.close()

# Create two seperate lists
list1 = []
list2 = []
i = 0
for x in input:
    if i % 2:
        list2.append(int(x))
    else:
        list1.append(int(x))
    i += 1

# Find similarities and save values
check = 0
similarities = 0
for x in list1:
    similarities += list1[check] * list2.count(list1[check])
    check += 1

print(f"Total similarities: {similarities}")