file = open("input.txt", "r")
content = [int(x) for x in file]
count = 0
for a, b in zip(content, content[1:]):
    if(a < b):
        count += 1
print(count)