from heapq import heappop, heappush
MOD = 20171109
T = int(input())
for TC in range(1, T+1):
    N, A = map(int, input().split())
    res = 0
    small = []  # max-heap
    big = [A]   # min-heap

    for i in range(1, N+1):
        X, Y = map(int, input().split())
        if X > Y:
            X, Y = Y, X
        if Y <= big[0]:
            heappush(small, -X)
            heappush(small, -Y)
            tmp = -heappop(small)
            heappush(big, tmp)
        elif X <= big[0] < Y:
            heappush(small, -X)
            heappush(big, Y)
        else:
            heappush(big, X)
            heappush(big, Y)
            tmp = heappop(big)
            heappush(small, -tmp)

        res += (big[0] % MOD)

    print(f'#{TC} {res % MOD}')