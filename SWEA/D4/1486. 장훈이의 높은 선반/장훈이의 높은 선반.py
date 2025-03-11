from itertools import combinations

T = int(input())

for TC in range(T):
    N, B = map(int, input().split())
    HEIGHTS = list(map(int, input().split()))

    res = B
    for i in range(1, N+1):
        nCr = combinations(range(N), i)
        for comb in nCr:
            tmp = 0
            for cc in comb:
                tmp += HEIGHTS[cc]
            if tmp >= B:
                res = min(res, abs(tmp-B))
    print(f'#{TC+1} {res}')