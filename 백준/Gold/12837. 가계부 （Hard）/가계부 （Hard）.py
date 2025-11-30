import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
LEN = 1
while LEN < N:
    LEN <<= 1

tree = [0] * (LEN * 2)

out = []
for _ in range(Q):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        idx = a + LEN - 1
        tree[idx] += b
        idx >>= 1
        while idx:
            tree[idx] = tree[idx*2] + tree[idx*2 + 1]
            idx >>= 1
    else:
        l, r = a + LEN - 1, b + LEN - 1
        ret = 0
        while l <= r:
            if l & 1:
                ret += tree[l]
                l += 1
            if not r & 1:
                ret += tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        out.append(str(ret))

print('\n'.join(out))