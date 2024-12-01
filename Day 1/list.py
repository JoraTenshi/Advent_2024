#PART 1

file = open("list", "r")
lines = file.readlines()
right_list = []
left_list = []
for line in lines:
	left_list.append(int(line.split("   ")[0]))
	right_list.append(int(line.split("   ")[1]))
file.close()
right_list.sort()
left_list.sort()
count = 0
for i in range(0, len(right_list)):
	diff = left_list[i] - right_list[i]
	count += diff if diff > 0 else -diff
print(f"Part 1: {count}")

#PART 2

count = 0
for i in range(0, len(right_list)):
	count += left_list[i] * right_list.count(left_list[i])
print(f"Part 2: {count}")