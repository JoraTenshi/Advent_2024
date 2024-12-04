#Part 1

file = open("corrupt_data.txt", 'r')
lines = file.readlines()
file.close()
result = 0
for line in lines:
    split = line.split('mul(')[1:]
    for group in split:
        pair = group.split(")", maxsplit=1)[0]
        try:
            first_number, second_number = pair.split(",", maxsplit = 1)
        except ValueError:
            continue

        if (first_number.isdigit()) and (second_number.isdigit()):
            result += int(first_number) * int(second_number)
print(f"Part 1: {result}")

#Part 2

