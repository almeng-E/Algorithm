import sys
input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        p[root_a] = root_b


N, Q = map(int, input().split())

p = [i for i in range(N+1)]
logs = []
for i in range(1, N+1):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, y, i))
logs.sort()


right = logs[0][1]
last_id = logs[0][3]

for i in range(1, N):
    nxt = logs[i]
    if nxt[0] <= right:
        union(nxt[3], last_id)
        right = max(nxt[1], right)
    else:
        last_id = nxt[3]
        right = nxt[1]

for _ in range(Q):
    a, b = map(int, input().split())
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        print(1)
    else:
        print(0)
