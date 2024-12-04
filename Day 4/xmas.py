#Part 1

file = open("xmasu.txt", "r")
lines = file.readlines()
file.close()

grid, result = [line.strip() for line in lines], 0
for y in range(len(grid)):
    for x in range(len(grid)):
        if grid[y][x] == 'X':
            for i in range(-1 if y > 2 else 0, 2 if y < len(grid) - 3 else 1):
                for j in range(-1 if x > 2 else 0, 2 if x < len(grid) - 3 else 1):
                    if grid[y + i][x + j] == 'M' and grid[y + 2 * i][x + 2 * j] == 'A' and grid[y + 3 * i][x + 3 * j] == 'S':
                        result += 1
print(f"Part 1: {result}")

#Part 2

grid = [line.strip() for line in lines]
result = sum([1 for y in range(1, len(grid) - 1) for x in range(1, len(grid) - 1) if grid[y][x] == 'A'
and {grid[y - 1][x - 1], grid[y + 1][x + 1]} == {'M', 'S'} and {grid[y + 1][x - 1], grid[y - 1][x + 1]} == {'M', 'S'}])
print(f"Part 2: {result}")