import sys
input = sys.stdin.readline


from itertools import combinations
from collections import deque


def is_connected(comb):
    q = deque()
    q.append(comb[0])
    v = {comb[0]}
    comb = set(comb)

    while q:
        cur = q.popleft()
        x, y = cur//5, cur%5
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            nxt = nx*5 + ny
            if nxt in comb and nxt not in v:
                v.add(nxt)
                q.append(nxt)
    return len(v) == 7


board = [input().rstrip() for _ in range(5)]
ans = 0
nCr = combinations(range(25), 7)
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
for comb in nCr:
    s_cnt = 0
    y_cnt = 0

    for x in comb:
        i = x // 5
        j = x % 5
        if board[i][j] == 'S':
            s_cnt += 1
        else:
            y_cnt += 1

        if y_cnt >= 4:
            break
    if s_cnt < 4:
        continue

    if is_connected(comb):
        ans += 1
print(ans)

