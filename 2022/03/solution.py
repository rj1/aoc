import os
import string

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")
chars = string.ascii_letters

total = 0
for line in lines:
    n = len(line)
    for c in chars:
        if (c in line[: n // 2]) and (c in line[n // 2 :]):
            total += chars.index(c) + 1

print(total)

total = 0
for i in range(len(lines) // 3):
    for c in chars:
        if c in lines[3 * i] and c in lines[3 * i + 1] and c in lines[3 * i + 2]:
            total += chars.index(c) + 1

print(total)
