import sys
input = sys.stdin.readline

from heapq import heappop, heappush
N = int(input())

arr = [0] + list(map(int, input().split()))
hq = []
v = [0] * (N+1)
for i in range(1, N+1):
    heappush(hq, (arr[i], i, v[i]))

M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))

    if q[0] == 1:
        i, j = q[1:]
        arr[i] = j
        v[i] += 1
        heappush(hq, (arr[i], i, v[i]))

    else:
        while hq and v[hq[0][1]] != hq[0][2]:
            heappop(hq)
        print(hq[0][1])