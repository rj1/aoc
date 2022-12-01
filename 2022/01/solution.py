import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

elves = []
for elf in input.split("\n\n"):
    cc = 0
    for c in elf.split("\n"):
        cc += int(c)
    elves.append(cc)

elves = sorted(elves)

print(elves[1])
print(elves[-1] + elves[-2] + elves[-3])
