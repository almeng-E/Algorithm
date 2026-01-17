import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [[0, 0] for _ in range(SIZE)]

for i in range(N):
    tree[i+LEN][0] = arr[i]
for i in range(LEN-1, 0, -1):
    tmp = []
    tmp.extend(tree[i*2])
    tmp.extend(tree[i*2 + 1])
    tmp.sort(reverse=True)
    tree[i] = tmp[:2]


M = int(input())
for _ in range(M):
    cmd = map(int, input().split())
    if next(cmd) == 1:
        idx = next(cmd)+LEN-1
        tree[idx][0] = next(cmd)
        idx >>= 1
        while idx:
            tmp = []
            tmp.extend(tree[idx * 2])
            tmp.extend(tree[idx * 2 + 1])
            tmp.sort(reverse=True)
            tree[idx] = tmp[:2]
            idx >>= 1

    else:
        l = next(cmd) + LEN - 1
        r = next(cmd) + LEN - 1
        tmp = []
        while l <= r:
            if l&1:
                tmp.extend(tree[l])
                l += 1
            if not (r&1):
                tmp.extend(tree[r])
                r -= 1
            l >>= 1
            r >>= 1

        tmp.sort(reverse=True)
        print(sum(tmp[:2]))