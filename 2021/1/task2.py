file = open("input.txt", "r")
content = [int(x) for x in file]
count = 0
for a, b, c, d in zip(content, content[1:], content[2:], content[3:]):
    if(a + b + c < b + c + d):
        count += 1
print(count)