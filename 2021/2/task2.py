file = open("input.txt")
horizontal = 0
depth = 0
aim = 0
content = [(x[:-3], int(x[-2:-1])) for x in file]
for (direction, X) in content:
    if(direction == "forward"):
        horizontal += X
        depth += (aim * X)
    elif(direction == "down"):
        aim += X
    elif(direction == "up"):
        aim -= X
print(horizontal * depth)