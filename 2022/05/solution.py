import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

sections = input.split("\n\n")
# crates = sections[0]
moves = sections[1].split("\n")

stacks = {
    1: ["N", "W", "B"],
    2: ["B", "M", "D", "T", "P", "S", "Z", "L"],
    3: ["R", "W", "Z", "H", "Q"],
    4: ["R", "Z", "J", "V", "D", "W"],
    5: ["B", "M", "H", "S"],
    6: ["B", "P", "V", "H", "J", "N", "G", "L"],
    7: ["S", "L", "D", "H", "F", "Z", "Q", "J"],
    8: ["B", "Q", "G", "J", "F", "S", "W"],
    9: ["J", "D", "C", "S", "M", "W", "Z"]
}

for move in moves:
    parts = move.split(" ")
    num = int(parts[1])
    start = int(parts[3])
    end = int(parts[5])

    # part 1
    # stacks[end] = stacks[start][:num][::-1] + stacks[end]
    # stacks[start] = stacks[start][num:]

    # part 2
    stacks[end] = stacks[start][:num] + stacks[end]
    stacks[start] = stacks[start][num:]

order = ""
for i in range(1, 10):
    if len(stacks[i]) > 0:
        order += stacks[i][0]

print(order)
