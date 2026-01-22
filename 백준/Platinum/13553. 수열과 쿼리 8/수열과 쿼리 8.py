import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
M = int(input())
Q = []
for i in range(M):
    l, r = map(int, input().split())
    Q.append((l, r, i))
sqrtN = int(N**0.5)
Q.sort(key=lambda x: (x[0]//sqrtN, x[1] if (x[0]//sqrtN)//2 == 0 else -x[1]))


LEN = 1
while LEN < 100_001:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
ans = [0] * M
cnt = 0
l, r = 1, 0

def add(idx):
    while idx:
        tree[idx] += 1
        idx >>= 1

def remove(idx):
    while idx:
        tree[idx] -= 1
        idx >>= 1

def get(idx):
    global K
    ret = 0
    l = max(LEN, idx-K)
    r = min(SIZE-1, idx+K)
    while l <= r:
        if l&1:
            ret += tree[l]
            l += 1
        if not (r&1):
            ret += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return ret

for ql, qr, qi in Q:
    while ql < l:
        l -= 1
        idx = arr[l] + LEN
        cnt += get(idx)
        add(idx)

    while l < ql:
        idx = arr[l] + LEN
        remove(idx)
        cnt -= get(idx)
        l += 1

    while r < qr:
        r += 1
        idx = arr[r] + LEN
        cnt += get(idx)
        add(idx)

    while qr < r:
        idx = arr[r] + LEN
        remove(idx)
        cnt -= get(idx)
        r -= 1
    ans[qi] = cnt
print('\n'.join(map(str, ans)))

