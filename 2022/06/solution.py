import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

for i in range(1, len(input)):
    # c = 4  # part 1
    c = 14  # part 2
    u = set(input[i - (c - 1) : i + 1])
    if len(u) == c:
        print(i + 1)
        break
