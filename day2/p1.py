
pos = 0
depth = 0

for line in open("input.txt"):
    cmd = line.split(" ")
    if cmd[0].strip() == "forward":
        pos += int(cmd[1])
    if cmd[0].strip() == "up":
        depth -= int(cmd[1])
    if cmd[0].strip() == "down":
        depth += int(cmd[1])

print(pos * depth)