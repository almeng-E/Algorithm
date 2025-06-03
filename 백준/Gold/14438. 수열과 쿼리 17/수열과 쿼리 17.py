import sys
input = sys.stdin.readline

def main():
    N = int(input())
    LEN = 1
    while LEN < N:
        LEN <<= 1
    SIZE = LEN << 1

    tree = [float('inf')] * SIZE

    tree[LEN: LEN+N] = map(int, input().split())

    for i in range(LEN-1, 0, -1):
        tree[i] = min(tree[(i<<1)], tree[(i<<1) + 1])

    M = int(input())
    for _ in range(M):
        a, b, c = map(int, input().split())
        if a == 1:
            idx = b-1+LEN
            tree[idx] = c
            idx >>= 1
            while idx:
                tree[idx] = min(tree[(idx << 1)], tree[(idx << 1) + 1])
                idx >>= 1

        elif a == 2:
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

main()
