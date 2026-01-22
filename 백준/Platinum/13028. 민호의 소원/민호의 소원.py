import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
Q = []
for i in range(M):
    l, r = map(int, input().split())
    Q.append((l, r, i))
sqrtN = int(N**0.5)
Q.sort(key=lambda x: (x[0]//sqrtN, x[1]))

l, r = 1, 0
ans = [0] * M
cnt = [0] * 100_001
cur = 0

def add(idx):
    global cur
    v = arr[idx]
    cnt[v] += 1
    if cnt[v] == 3:
        cur += 1

def remove(idx):
    global cur
    v = arr[idx]
    cnt[v] -= 1
    if cnt[v] == 2:
        cur -= 1


for ql, qr, idx in Q:
    while ql < l:
        l -= 1
        add(l)
    while l < ql:
        remove(l)
        l += 1
    while r < qr:
        r += 1
        add(r)
    while qr < r:
        remove(r)
        r -= 1

    ans[idx] = cur

print('\n'.join(map(str, ans)))
