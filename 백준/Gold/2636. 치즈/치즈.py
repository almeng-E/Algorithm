import sys
input = sys.stdin.readline


from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

starts = []
for i in range(M):
    starts.append((0, i))
    starts.append((N-1, i))
for i in range(N):
    starts.append((i, 0))
    starts.append((i, M-1))

steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

ans = 0
last = 0
while True:
    v = [[0] * M for _ in range(N)]
    nxt = []
    for x, y in starts:
        if v[x][y]:
            continue
        q = deque()
        q.append((x, y))
        v[x][y] = 1
        while q:
            x, y = q.popleft()
            for dx, dy in steps:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M or v[nx][ny]:
                    continue
                v[nx][ny] = 1
                if board[nx][ny]:
                    nxt.append((nx, ny))
                else:
                    q.append((nx, ny))
    if nxt:
        ans += 1
        last = len(nxt)
        for x, y in nxt:
            board[x][y] = 0
    else:
        break
print(ans)
print(last)