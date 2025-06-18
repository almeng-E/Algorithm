import sys
input = sys.stdin.readline
def main():
    N, M = map(int, input().split())

    LEN = 1
    while LEN < N:
        LEN <<= 1
    SIZE = LEN << 1

    tree = [0] * SIZE


    for _ in range(M):
        cmd, a, b = map(int, input().split())

        if cmd == 0:
            # get-range
            if a > b:
                a, b = b, a

            left = a + LEN - 1
            right = b + LEN - 1
            res = 0

            while left <= right:
                if left & 1:
                    res += tree[left]
                    left += 1
                if not right & 1:
                    res += tree[right]
                    right -= 1
                left >>= 1
                right >>= 1

            print(res)

        elif cmd == 1:
            # update-point
            idx = a + LEN - 1
            tree[idx] = b
            idx >>= 1
            while idx:
                tree[idx] = tree[(idx << 1)] + tree[(idx << 1) + 1]
                idx >>= 1

main()