import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)

ret = []
tmp = sorted(arr)
compressed = [bisect_left(tmp, e) for e in arr]

LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN*2
tree = [0] * SIZE

for i in range(N):
    ID = compressed[i]

    l = LEN + ID
    r = SIZE - 1
    cnt = 1
    while l <= r:
        if l & 1:
            cnt += tree[l]
            l += 1
        if not (r & 1):
            cnt += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    ret.append(cnt)

    ID += LEN
    while ID:
        tree[ID] += 1
        ID >>= 1

print('\n'.join(map(str, ret)))