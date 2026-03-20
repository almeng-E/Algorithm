import sys
input = sys.stdin.readline


N, M = map(int, input().split())
# 0은 빈 칸, 6은 벽, 1~5는 CCTV
board = [list(map(int, input().split())) for _ in range(N)]
steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

seen = [[0] * M for _ in range(N)]
CCTV = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            seen[i][j] = 100
            if board[i][j] != 6:
                CCTV.append((board[i][j], i, j))


def count():
    ret = 0
    for i in range(N):
        for j in range(M):
            if seen[i][j] == 0:
                ret += 1
    # print(f'DEBUG!! ans: {ans} vs ret:{ret} ')
    # for r in seen:
    #     print(*r)
    # print()
    return ret


def activate(x, y, dx, dy):
    while 0 <= x < N and 0 <= y < M and board[x][y] != 6:
        seen[x][y] += 1
        x += dx
        y += dy


def deactivate(x, y, dx, dy):
    while 0 <= x < N and 0 <= y < M and board[x][y] != 6:
        seen[x][y] -= 1
        x += dx
        y += dy


def simulate(cctv_idx):
    global ans
    if cctv_idx == len(CCTV):
        ans = min(ans, count())
        return
    c_type, x, y = CCTV[cctv_idx]

    for d_set in dirs[c_type]:
        for d_i in d_set:
            dx, dy = steps[d_i]
            nx, ny = x+dx, y+dy
            activate(nx, ny, dx, dy)

        simulate(cctv_idx + 1)

        for d_i in d_set:
            dx, dy = steps[d_i]
            nx, ny = x+dx, y+dy
            deactivate(nx, ny, dx, dy)

ans = N*M
simulate(0)
print(ans)
