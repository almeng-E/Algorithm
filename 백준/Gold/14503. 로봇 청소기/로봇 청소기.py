import sys
input = sys.stdin.readline

def check(x, y):
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if board[nx][ny] == 0 and not cleaned[nx][ny]:
            return 1
    return 0


N, M = map(int, input().split())
x, y, d = map(int, input().split())

# 북 동 남 서
steps = ((-1, 0), (0, 1), (1, 0), (0, -1))
board = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[0] * M for _ in range(N)]
ans = 0
while True:
    if not cleaned[x][y]:
        cleaned[x][y] = 1
        ans += 1

    if not check(x, y):
        bd = (d+2)%4
        bx, by = x+steps[bd][0], y+steps[bd][1]
        if board[bx][by]:
            break
        else:
            x, y = bx, by
            continue
    else:
        d = (d-1)%4
        nx, ny = x+steps[d][0], y+steps[d][1]
        if board[nx][ny] == 0 and not cleaned[nx][ny]:
            x, y = nx, ny
            continue

print(ans)