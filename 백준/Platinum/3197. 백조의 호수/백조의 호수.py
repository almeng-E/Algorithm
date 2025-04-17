import sys
input = sys.stdin.readline



from collections import deque


def set_groups(x, y):
    global g_cnt, N, M
    if board[x][y] == 'L':
        target_groups.append(g_cnt)

    board[x][y] = g_cnt

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if board[nx][ny] == '.':
                board[nx][ny] = g_cnt
                queue.append((nx, ny))
            elif board[nx][ny] == 'L':
                target_groups.append(g_cnt)
                board[nx][ny] = g_cnt
                queue.append((nx, ny))
            elif board[nx][ny] == 'X':
                next_melt.add((nx, ny))


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    r_a = find(a)
    r_b = find(b)
    if r_a == r_b:
        return
    else:
        p[r_a] = r_b


def change():
    tmp_melt = set()
    for x, y in next_melt:
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if board[nx][ny] == 'X':
                tmp_melt.add((nx, ny))
                continue

            # 그룹이 아직 아니라면 -> 바꿔주기만 함
            if board[x][y] == 'X':
                board[x][y] = board[nx][ny]


            # 벌써 그룹임 -> 근데 다른 그룹을 만남 -> UnionFind
            if board[x][y] != 'X':
                union(board[x][y], board[nx][ny])

    return tmp_melt


steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 그룹화 및 분리집합 부모 저장
p = [0]
target_groups = []
g_cnt = 1
# 후보 찾기
next_melt = set()

for i in range(N):
    for j in range(M):
        if board[i][j] == '.' or board[i][j] == 'L':
            set_groups(i, j)
            p.append(g_cnt)
            g_cnt += 1

# for row in board:
#     print(*row)
# print(next_melt)


res = 0
while find(target_groups[0]) != find(target_groups[1]):
    res += 1

    next_melt = change()



print(res)