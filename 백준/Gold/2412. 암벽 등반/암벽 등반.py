import sys
input = sys.stdin.readline
from collections import deque

N, T = map(int, input().split())

holds = set(tuple(map(int, input().split())) for _ in range(N))

queue = deque()
queue.append((0, 0, 0))
res = -1
steps = (-2, -1, 0, +1, +2)
while queue:
    x, y, c_dist = queue.popleft()
    if y == T:
        res = c_dist
        break

    for dx in steps:
        for dy in steps:
            nx, ny = x+dx, y+dy
            if 0 <= nx and 0 <= ny and (nx, ny) in holds:
                holds.remove((nx, ny))
                queue.append((nx, ny, c_dist + 1))

print(res)