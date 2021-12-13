
pos = 0
depth = 0
aim = 0

for line in open("input.txt"):
    cmd = line.split(" ")
    if cmd[0].strip() == "forward":
        pos += int(cmd[1])
        depth += aim * int(cmd[1])
    if cmd[0].strip() == "up":
        aim -= int(cmd[1])
    if cmd[0].strip() == "down":
        aim += int(cmd[1])

print(pos * depth)