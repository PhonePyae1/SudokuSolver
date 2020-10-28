board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]


def solve(board):
    if findEmpty(board) == 0:
        return True
    else:
        pos = findEmpty(board)
        row, col = pos

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


def valid(board, n, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == n and pos[1] != i:
            return False

    # check Column
    for i in range(len(board)):
        if board[i][pos[1]] == n and pos[0] != i:
            return False

    x = pos[1] // 3  # 2
    y = pos[0] // 3  # 0
    # check box

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == n and (i, j) != i:
                return False

    return True


def printBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return 0



print("Unsolved Version")
printBoard(board)
solve(board)
print("----------------------------------")
print("Solved Version")
printBoard(board)
