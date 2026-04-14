import sys
input = sys.stdin.readline
from collections import deque

LIMIT = list(map(int, input().split()))
v = [[False] * (LIMIT[1] + 1) for _ in range(LIMIT[0] + 1)]
pour = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
ans = []

q = deque()
q.append([0, 0, LIMIT[2]])
v[0][0] = True
ans.append(LIMIT[2])

while q:
    cur = q.popleft()

    for x, y in pour:
        nxt = cur[:]
        amount = min(cur[x], LIMIT[y]-cur[y])
        if amount > 0:
            nxt[x] -= amount
            nxt[y] += amount

        if not v[nxt[0]][nxt[1]]:
            v[nxt[0]][nxt[1]] = True
            q.append(nxt)
            if nxt[0] == 0:
                ans.append(nxt[2])

print(*sorted(ans))