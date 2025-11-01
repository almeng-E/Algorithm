import sys
input = sys.stdin.readline

def b_id(x, y):
    return (x // 3) * 3 + (y // 3)


def sudoku(IDX):
    if IDX == len(zeros):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()

        exit()

    i, j = zeros[IDX]
    b = b_id(i, j)

    for cand in range(1, 10):
        if not row[i][cand] and not col[j][cand] and not bucket[b][cand]:
            board[i][j] = cand
            row[i][cand] = True
            col[j][cand] = True
            bucket[b][cand] = True

            sudoku(IDX+1)

            board[i][j] = 0
            row[i][cand] = False
            col[j][cand] = False
            bucket[b][cand] = False


board = [list(map(int, input().rstrip())) for _ in range(9)]
bucket = [[False for _ in range(10)] for _ in range(9)]
col = [[False for _ in range(10)] for _ in range(9)]
row = [[False for _ in range(10)] for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            b = b_id(i, j)
            bucket[b][board[i][j]] = True
            row[i][board[i][j]] = True
            col[j][board[i][j]] = True
        else:
            zeros.append((i, j))

sudoku(0)