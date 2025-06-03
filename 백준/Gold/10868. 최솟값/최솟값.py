import sys
input = sys.stdin.readline

N, M = map(int, input().split())
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1
tree = [float('inf')] * SIZE

for i in range(N):
    tree[i+LEN] = int(input())

for i in range(LEN-1, 0, -1):
    tree[i] = min(tree[(i<<1)], tree[(i<<1) + 1])

for _ in range(M):
    b, c = map(int, input().split())

    res = float('inf')
    l = b - 1 + LEN
    r = c - 1 + LEN
    while l <= r:
        if l & 1:
            res = min(tree[l], res)
            l += 1
        if not r & 1:
            res = min(tree[r], res)
            r -= 1
        l >>= 1
        r >>= 1
    print(res)

    