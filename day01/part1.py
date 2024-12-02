
file = open("input.txt")
input = file.read().split()
file.close()

list1 = []
list2 = []

i = 0
for x in input:
    if i % 2:
        list2.append(int(x))
    else:
        list1.append(int(x))
    i += 1


list1.sort()
list2.sort()

check = 0
total = 0
for x in list1:
    total += abs(list1[check] - list2[check])
    check += 1

print(f"Total distance between the two lists is: {total}")