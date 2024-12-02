def problem_dampener(x, problems):
	global safe
	numbers.pop(x)
	x = -1
	problems += 1
	safe = True
	return problems, safe, x

def checker():
	global increasing, diff, safe
	if numbers[x] < numbers[x + 1] and x == 0:
		increasing = True
	elif x == 0:
		increasing = False
	if increasing:
		diff = numbers[x] - numbers[x + 1]
		if 0 > diff > -4:
			safe = True
		else:
			safe = False
	elif not increasing:
		diff = numbers[x] - numbers[x + 1]
		if 0 < diff < 4:
			safe = True
		else:
			safe = False
	return safe

#Part 1

file = open("report.txt", "r")
lines = file.readlines()
file.close()
count = 0

for line in lines:
	numbers = line.split(" ")
	numbers = [int(i) for i in numbers]
	safe = True
	for x in range(0, len(numbers)):
		if x + 1 < len(numbers) and safe:
			safe = checker()
			if not safe:
				break
	if safe:
		count += 1
print(f"Part 1: {count}")

#Part 2

count = 0

for line in lines:
	numbers = line.split(" ")
	numbers = [int(i) for i in numbers]
	safe = True
	problems = 0
	x = 0
	while x in range(0, len(numbers)) and problems < 2:
		if x + 1 < len(numbers) and safe:
			safe = checker()
			if not safe and problems == 0 and x == 1:
				problems, safe, x = problem_dampener(x - 1, problems)
			elif not safe and problems == 0 and x == 0:
				problems, safe, x = problem_dampener(x, problems)
			elif not safe and problems == 0:
				problems, safe, x = problem_dampener(x + 1, problems)
			elif not safe and problems == 1:
				problems += 1
		x += 1
	if safe and problems <= 1:
		count += 1
print(f"Part 2: {count}")