import sys
input = sys.stdin.readline

from heapq import heappop, heappush


MOD = 1_000_000_007
T = int(input())
for _ in range(T):
    N = int(input())
    hq = []
    for i in map(int, input().split()):
        heappush(hq, i)
    res = 1
    for _ in range(N-1):
        a = heappop(hq)
        b = heappop(hq)
        res *= a*b
        res %= MOD
        heappush(hq, a*b)
    print(res)