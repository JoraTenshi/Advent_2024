#Part 1

file = open("map.txt", "r")
lines = file.readlines()
file.close()
rows = len(lines)
cols = len(lines[0])

directions = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
pos = ()
facing = ()
for i in range(rows):
    for j in range(cols):
        if lines[i][j] in directions:
            initial_pos = (i, j)
            facing = directions[lines[i][j]]

i, j = initial_pos
x, y = facing
new_pos = (i + x, j + y)
inside = True
while inside:
