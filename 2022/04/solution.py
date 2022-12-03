import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

pairs = []
for line in lines:
    a, b = line.split(",")
    pairs.append((a, b))

count = 0
for a, b in pairs:
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))

    if (a1 <= b2 and a2 >= b1) or (b1 <= a2 and b2 >= a1):
        count += 1

print(count)
