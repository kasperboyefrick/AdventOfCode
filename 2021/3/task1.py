file = open("input.txt")
content = [x for x in file]
finalBitString = ""
invertedBitString = ""
for x in range(0, 12):
    one = 0
    zero = 0
    for y in content:
        if(y[x] == "1"):
            one += 1
        else:
            zero += 1
    if(one > zero):
        finalBitString += "1"
        invertedBitString += "0"
    else:
        finalBitString += "0"
        invertedBitString += "1"

print(finalBitString)
print(invertedBitString)
print(int(finalBitString, 2) * int(invertedBitString, 2))