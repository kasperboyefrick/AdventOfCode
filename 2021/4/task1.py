file = open("input.txt")
numbers = [int(x) for x in file.readline().strip().split(",")]

boards = []
breaking = False
while True:
    file.readline()
    board = []
    for x in range(0,4):
        line = file.readline()
        if len(line) == 0:
            breaking = True
            break
        board.append(line.strip().split())
    if breaking:
        break
    boards.append(board)


print(numbers)
print(boards)