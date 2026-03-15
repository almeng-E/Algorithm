import sys
input = sys.stdin.readline

def blow(x, y, d):
    sand = board[x][y]
    if sand == 0:
        return 0

    board[x][y] = 0
    out = 0
    spread = 0

    ld = (d + 1) % 4
    rd = (d - 1) % 4
    bd = (d + 2) % 4

    LR = (ld, rd)
    moves = []

    # 1%
    for i in LR:
        cx = x + direction[bd][0] + direction[i][0]
        cy = y + direction[bd][1] + direction[i][1]
        moves.append((cx, cy, 1))

    # 7%
    for i in LR:
        cx = x + direction[i][0]
        cy = y + direction[i][1]
        moves.append((cx, cy, 7))

    # 2%
    for i in LR:
        cx = x + 2 * direction[i][0]
        cy = y + 2 * direction[i][1]
        moves.append((cx, cy, 2))

    nx = x + direction[d][0]
    ny = y + direction[d][1]

    # 10%
    for i in LR:
        cx = nx + direction[i][0]
        cy = ny + direction[i][1]
        moves.append((cx, cy, 10))

    # 5%
    cx = nx + direction[d][0]
    cy = ny + direction[d][1]
    moves.append((cx, cy, 5))

    # 퍼뜨리기
    for cx, cy, p in moves:
        amount = sand * p // 100
        spread += amount
        if 0 <= cx < N and 0 <= cy < N:
            board[cx][cy] += amount
        else:
            out += amount

    # a
    if 0 <= nx < N and 0 <= ny < N:
        board[nx][ny] += sand - spread
    else:
        out += sand - spread

    return out


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

D = 0
L = 0
direction = ((0, -1), (1, 0), (0, 1), (-1, 0))
length = (1, 0, 1, 0)

ans = 0
x, y = N//2, N//2
while (x, y) != (0, 0):
    L += length[D]
    for _ in range(L):
        x += direction[D][0]
        y += direction[D][1]
        ans += blow(x, y, D)
        if x == 0 and y == 0:
            break
    D += 1
    D %= 4

print(ans)
