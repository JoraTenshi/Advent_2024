#Part 1

from functools import cmp_to_key
result = 0
rules, pages = open("list.txt").read().strip().split("\n\n")
ruling = []
for rule in rules.split():
    ruling.append(tuple(map(int, rule.split("|"))))
paging = []
for page in pages.split():
    paging.append(list(map(int, page.split(","))))
key = cmp_to_key(lambda x, y: ((y, x) in ruling) - ((x, y) in ruling))
for row in paging:
    if row == (new_row := sorted(row, key=key)):
        result += new_row[len(row) // 2]
print(result)

#Part 2
result = 0
for row in paging:
    if row != (new_row := sorted(row, key=key)):
        result += new_row[len(row) // 2]
print(result)
