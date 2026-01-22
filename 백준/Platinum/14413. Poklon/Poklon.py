import sys
input = sys.stdin.readline

def add(i):
    global cur
    v = arr[i]
    idx = v_idx_map[v]
    if cnt[idx] == 2:
        cur -= 1
    elif cnt[idx] == 1:
        cur += 1
    cnt[idx] += 1

def remove(i):
    global cur
    v = arr[i]
    idx = v_idx_map[v]
    if cnt[idx] == 2:
        cur -= 1
    elif cnt[idx] == 3:
        cur += 1
    cnt[idx] -= 1


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
Q = []
for i in range(M):
    L, R = map(int, input().split())
    Q.append((L, R, i))
sqrtN = int(N**0.5)
Q.sort(key=lambda x: (x[0]//sqrtN, x[1]))

compressed = set(arr)
v_idx_map = {v: i for i, v in enumerate(compressed)}

cnt = [0] * len(compressed)
ans = [0] * M
cur = 0
l, r = 1, 0
for ql, qr, i in Q:
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

    ans[i] = cur

print('\n'.join(map(str, ans)))