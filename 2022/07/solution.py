import os
from collections import defaultdict

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

dirs = defaultdict(int)
path = []
for line in lines:
    parts = line.strip().split()
    if parts[1] == "cd":
        if parts[2] == "..":
            path.pop()
        else:
            path.append(parts[2])
    elif parts[1] == "ls":
        continue
    elif parts[0] == "dir":
        continue
    else:
        size = int(parts[0])
        # print(size)
        # add dirs
        for i in range(1, len(path) + 1):
            dirs["/".join(path[:i])] += size

# for dir in dirs:
#     print(dir)

total = dirs["/"]
need = total - 40000000

part1 = 0
part2 = 9999999
# dir, size
for k, v in dirs.items():
    # print(k,v)
    if v <= 100000:
        part1 += v
    if v >= need:
        part2 = min(part2, v)

print(part1)
print(part2)
