import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

p = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8,
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9,
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7,
    },
}

p1 = []
p2 = []

for line in lines:
    cc, c = line.split(" ")
    p1.append(cc)
    p2.append(c)

count = 0
for i, c in enumerate(p2):
    count += p[p1[i]][c]

print(count)
