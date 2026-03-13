import sys
input = sys.stdin.readline

from collections import deque
def solve():
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    DELTA = ((0, 1), (1, 0), (-1, 0), (0, -1))
    ans = 0
    while True:
        v = [[0 for _ in range(N)] for _ in range(N)]
        groups = []
        for i in range(N):
            for j in range(N):
                if v[i][j]: continue

                q = deque()
                q.append((i, j))
                v[i][j] = 1
                tmp = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for dx, dy in DELTA:
                        nx, ny = x+dx, y+dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= N or v[nx][ny]:
                            continue
                        if L <= abs(board[nx][ny] - board[x][y]) <= R:
                            v[nx][ny] = 1
                            tmp.append((nx, ny))
                            q.append((nx, ny))
                if len(tmp) > 1:
                    groups.append(tmp)
        if not groups:
            break
        ans += 1

        for g in groups:
            p = 0
            for x, y in g:
                p += board[x][y]
            for x, y in g:
                board[x][y] = p//len(g)
    print(ans)
solve()