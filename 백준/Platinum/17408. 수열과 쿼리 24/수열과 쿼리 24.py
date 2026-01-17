import sys
input = sys.stdin.readline

def merge(a, b):
    x1, x2 = a
    y1, y2 = b
    if x1 > y1:
        return x1, max(y1, y2, x2)
    else:
        return y1, max(x1, x2, y2)

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    LEN = 1
    while LEN < N:
        LEN <<= 1
    SIZE = LEN << 1

    tree = [(0, 0) for _ in range(SIZE)]

    for i in range(N):
        tree[i+LEN] = (arr[i], 0)
    for i in range(LEN-1, 0, -1):
        tree[i] = merge(tree[i*2], tree[i*2+1])


    ret = []
    M = int(input())
    for _ in range(M):
        cmd = map(int, input().split())
        if next(cmd) == 1:
            idx = next(cmd)+LEN-1
            tree[idx] = (next(cmd), 0)
            idx >>= 1
            while idx:
                tree[idx] = merge(tree[idx*2], tree[idx*2+1])
                idx >>= 1

        else:
            l = next(cmd) + LEN - 1
            r = next(cmd) + LEN - 1
            tmp = [0, 0]
            while l <= r:
                if l&1:
                    tmp = merge(tmp, tree[l])
                    l += 1
                if not (r&1):
                    tmp = merge(tmp, tree[r])
                    r -= 1
                l >>= 1
                r >>= 1

            ret.append(str(sum(tmp)))
    print('\n'.join(ret))

solve()
