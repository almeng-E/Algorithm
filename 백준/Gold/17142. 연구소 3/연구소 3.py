import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    v = []
    s = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                v.append((i, j))
            elif board[i][j] == 0:
                s += 1
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

    nCr = combinations(v, M)
    res = 50*50
    for comb in nCr:
        visited = [[-1] * (N+1) for _ in range(N)]
        q = deque()
        cnt = 0
        for vx, vy in comb:
            q.append((vx, vy))
            visited[vx][vy] = 0
        while q:
            x, y = q.popleft()

            for dx, dy in steps:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < N and 0 <= ny < N): continue
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    cnt += 1
                    visited[nx][ny] = visited[x][y] + 1
                    if cnt == s:
                        res = min(res, visited[nx][ny])
                        break
                    q.append((nx, ny))
                elif board[nx][ny] == 2 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    if s == 0:
        res = 0
    print(res if res != 2500 else -1)

solve()
