import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    A, B = map(int, input().split())

    manjok = [[0, 0, 0]]
    for _ in range(N):
        a, b, c, d = list(map(int, input().split()))
        manjok.append([max(a, b), c, d])
    DP = dict()
    DP[0] = {
        (0, 0, 0): 0,
        (0, 0, 1): 0,
        (0, 0, 2): 0,
    }
    for day in range(1, N+1):
        d = dict()
        for dt in range(3):
            dm = manjok[day][dt]
            for k, bm in DP[day-1].items():
                a, b, t = k

                if dt == 1 and t == 1:
                    continue
                if dt == 2 and a == A:
                    continue

                if dt == 0:
                    b += 1
                elif dt == 2:
                    a += 1

                if (a, b, dt) in d:
                    d[(a, b, dt)] = max(d[a, b, dt], bm + dm)
                else:
                    d[(a, b, dt)] = bm + dm

        DP[day] = d


    res = 0
    for k, v in DP[N].items():
        a, b, _ = k
        if a <= A and b >= B:
            res = max(res, v)
    print(res)
solution()