from heapq import heappop, heappush
N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]

dist = [[float('inf') for _ in range(N)] for _ in range(N)]

dist[0][0] = 0
hq = []
hq.append((0, 0, 0))

steps = ((0, 1), (1, 0), (-1, 0), (0, -1))

while hq:
    d, x, y = heappop(hq)

    if dist[x][y] < d:
        continue

    for dx, dy in steps:
        nx, ny = x+dx, y+dy

        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue

        if board[nx][ny] == 0:
            nd = d+1
        else:
            nd = d

        if dist[nx][ny] > nd:
            dist[nx][ny] = nd
            heappush(hq, (nd, nx, ny))

print(dist[N-1][N-1])