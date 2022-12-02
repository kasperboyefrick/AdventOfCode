import fileinput

array = [0]
for line in fileinput.input(files = "input"):
    if line.isspace():
        array.insert(0, 0)
    else:
        array[0] += int(line)

array.sort(reverse=True)
print(sum(array[:3]))