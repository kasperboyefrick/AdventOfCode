file = open("input.txt")
horizontal = 0
depth = 0
content = [(x[:-3], int(x[-2:-1])) for x in file]
for (direction, X) in content:
    if(direction == "forward"):
        horizontal += X
    elif(direction == "down"):
        depth += X
    elif(direction == "up"):
        depth -= X
print(horizontal * depth)