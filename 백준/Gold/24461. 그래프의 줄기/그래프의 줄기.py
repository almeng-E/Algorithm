import sys
input = sys.stdin.readline




N = int(input())
g = [[] for _ in range(N)]
cnt = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    cnt[a] += 1
    cnt[b] += 1

q = []
for i in range(N):
    if cnt[i] == 1:
        q.append(i)
        cnt[i] = -1

br = 0
for i in range(N):
    if cnt[i] >= 3:
        br += 1

if br == 0:
    print(*range(N))
    exit()

while q:
    touched = set()
    nq = []

    for cur in q:
        for nxt in g[cur]:
            if cnt[nxt] == -1:
                continue
            if cnt[nxt] == 3:
                br -= 1
            cnt[nxt] -= 1
            touched.add(nxt)

    if br == 0:
        break

    for v in touched:
        if cnt[v] == 1:
            nq.append(v)
            cnt[v] = -1
    q = nq

ans = []
for i in range(N):
    if cnt[i] != -1:
        ans.append(i)
print(*ans)