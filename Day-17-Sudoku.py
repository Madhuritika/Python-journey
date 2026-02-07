board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
def print_board():
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None
def valid(num, pos):
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True
def solve():
    find = find_empty()
    if not find:
        return True
    row, col = find

    for i in range(1,10):
        if valid(i, (row, col)):
            board[row][col] = i

            if solve():
                return True

            board[row][col] = 0

    return False
def game():
    while True:
        print_board()
        print("\nEnter row col number (1-9) or 0 0 0 to quit")

        row, col, num = map(int, input("Enter: ").split())

        if row == 0 and col == 0 and num == 0:
            print("Game Over 👋")
            break

        if board[row-1][col-1] != 0:
            print("Cell already filled!")
        elif valid(num, (row-1, col-1)):
            board[row-1][col-1] = num
        else:
            print("Invalid move!")
game()
