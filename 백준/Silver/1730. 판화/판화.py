import sys
input = sys.stdin.readline

N = int(input())
board = [[46 for _ in range(N)] for _ in range(N)]

cmd = input().rstrip()

steps = {
    'D': (1, 0),
    'U': (-1, 0),
    'R': (0, 1),
    'L': (0, -1),
}

# 46, 124, 45, 43 == . | - +
change_to = {
    'D': {
        46: 124,
        124: 124,
        45: 43,
        43: 43,
    },
    'U': {
        46: 124,
        124: 124,
        45: 43,
        43: 43,
    },
    'R': {
        46: 45,
        124: 43,
        45: 45,
        43: 43,
    },
    'L': {
        
        46: 45,
        124: 43,
        45: 45,
        43: 43,
    }
}

x, y = 0, 0
for m in cmd:
    dx, dy = steps[m]
    if not (0<= x+dx < N and 0 <= y+dy < N):
        continue
    board[x][y] = change_to[m][board[x][y]]

    x += dx
    y += dy
    board[x][y] = change_to[m][board[x][y]]


for row in board:
    for v in row:
        print(chr(v), end='')
    print()
