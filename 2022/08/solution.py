import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")


grid = []
for line in lines:
    grid.append(line)

rows = len(grid)
cols = len(grid[0])
org = [(-1, 0), (0, 1), (1, 0), (0, -1)]

part1 = 0
for row in range(rows):
    for c in range(cols):
        visible = False
        for (dorow, docol) in org:
            rowf = row
            colf = c
            ok = True
            while True:
                rowf += dorow
                colf += docol
                if not (0 <= rowf < rows and 0 <= colf < cols):
                    break
                if grid[rowf][colf] >= grid[row][c]:
                    ok = False
            if ok:
                visible = True
        if visible:
            part1 += 1

print(part1)

part2 = 0
for row in range(rows):
    for c in range(cols):
        total = 1
        for (dorow, docol) in org:
            distance = 1
            rowf = row + dorow
            colf = c + docol
            while True:
                if not (0 <= rowf < rows and 0 <= colf < cols):
                    distance -= 1
                    break
                if grid[rowf][colf] >= grid[row][c]:
                    break
                distance += 1
                rowf += dorow
                colf += docol
            total *= distance
        part2 = max(part2, total)

print(part2)
