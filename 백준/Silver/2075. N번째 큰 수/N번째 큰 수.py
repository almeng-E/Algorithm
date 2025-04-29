import sys
input = sys.stdin.readline
import heapq
N = int(input())
for i in range(N):
    if i == 0:
        hq = list(map(int,input().split()))
        heapq.heapify(hq)
        continue

    for j in map(int, input().split()):
        heapq.heappushpop(hq, j)

print(hq[0])