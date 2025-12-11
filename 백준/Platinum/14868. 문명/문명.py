import sys
input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    global cnt
    rta = find(a)
    rtb = find(b)
    if rta != rtb:
        p[rtb] = rta
        cnt -= 1


steps = ((0, 1), (1, 0), (-1, 0), (0, -1))
N, K = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(N)]

cnt = K
p = [i for i in range(K+1)]

q = []
for i in range(1, K+1):
    x, y = map(int, input().split())
    q.append((x-1, y-1))
    board[x-1][y-1] = i

days = 0
while q and cnt > 1:

    nq = []
    for x, y in q:
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] != 0 and find(p[board[nx][ny]]) != find(p[board[x][y]]):
                union(p[board[nx][ny]], p[board[x][y]])

    if cnt == 1:
        break
    days += 1

    for x, y in q:
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = find(p[board[x][y]])
                nq.append((nx, ny))

    q = nq.copy()

    # print(days)
    # for row in board:
    #     print(*row)
    # print(p)

print(days)

