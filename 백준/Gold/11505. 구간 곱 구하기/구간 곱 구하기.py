import sys
input = sys.stdin.readline
def main():
    N, M, K = map(int, input().split())
    MOD = 10**9 + 7

    LEN = 1
    while LEN <= N:
        LEN <<= 1
    SIZE = LEN << 1

    # make tree
    tree = [1] * SIZE
    for i in range(N):
        tree[i+LEN] = int(input())

    # set tree
    for i in range(LEN-1, 0, -1):
        tree[i] = (tree[(i << 1)] * tree[(i << 1) + 1]) % MOD

    # 쿼리 수행
    for _ in range(M+K):
        a, b, c = map(int, input().split())

        # update tree
        if a == 1:
            b = b - 1 + LEN  # 0-index and 트리 인덱스로 변환
            tree[b] = c
            b >>= 1

            while b >= 1:
                tree[b] = (tree[(b << 1)] * tree[(b << 1) + 1]) % MOD
                b >>= 1

        # get
        elif a == 2:
            left = b - 1 + LEN
            right = c - 1 + LEN

            res = 1
            while left <= right:
                if left & 1:
                    res *= tree[left]
                    res %= MOD
                    left += 1
                if not right & 1:
                    res *= tree[right]
                    res %= MOD
                    right -= 1

                left >>= 1
                right >>= 1

            print(res)
main()