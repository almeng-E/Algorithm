import sys
input = sys.stdin.readline


from heapq import heappop, heappush

N, L = map(int, input().split())
arr = list(map(int, input().split()))

res = []
curr = []
lazy = []

# 초반 ~ DL
for i in range(L):
    heappush(curr, arr[i])
    res.append(str(curr[0]))

# 후반 DL+1 ~
for i in range(L, N):
    heappush(lazy, arr[i-L])
    heappush(curr, arr[i])

    while lazy and lazy[0] == curr[0]:
        heappop(lazy)
        heappop(curr)
    
    res.append(str(curr[0]))
    
print(" ".join(res))


