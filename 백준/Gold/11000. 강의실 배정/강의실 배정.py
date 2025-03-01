import sys
import heapq

input = sys.stdin.readline

N = int(input())

courses = []
for _ in range(N):
    Si, Ti = map(int, input().split())
    courses.append((Si, Ti))

courses.sort(key=lambda x: (x[1], x[0]), reverse=True)

hq = []
heapq.heappush(hq, -1*(courses[0][0]))
for i in range(1, N):
    c_max = heapq.heappop(hq)
    if courses[i][1] > -c_max:
        heapq.heappush(hq, c_max)
    heapq.heappush(hq, -1*(courses[i][0]))

print(len(hq))