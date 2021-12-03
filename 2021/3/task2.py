file = open("input.txt")
content = [x[:-1] for x in file]
n = len(content[0])

oxygen = ""
scrubber = ""
temp = content.copy()
for x in range(0, n):
    one = 0
    zero = 0
    for y in temp:
        if(y[x] == "1"):
            one += 1
        else:
            zero += 1
    if(one >= zero):
        temp = list(filter(lambda number: number[x] == "1", temp))
    else:
        temp = list(filter(lambda number: number[x] == "0", temp))
    if(len(temp) == 1):
        break
oxygen = temp[0]

temp = content.copy()
for x in range(0, n):
    one = 0
    zero = 0
    for y in temp:
        if(y[x] == "1"):
            one += 1
        else:
            zero += 1
    print(temp)
    print(one < zero)
    if(one < zero):
        temp = list(filter(lambda number: number[x] == "1", temp))
    else:
        temp = list(filter(lambda number: number[x] == "0", temp))
    print(temp)
    print()
    if(len(temp) == 1):
        break
    print("loop")
scrubber = temp[0]
        
    

print(oxygen)
print(scrubber)
print(int(oxygen, 2) * int(scrubber, 2))