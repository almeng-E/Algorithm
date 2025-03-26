import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
INF = float('inf')
MAX = max(N, K)


time = [INF] * (MAX+ 2)
path_before = [-1 for _ in range(MAX + 2)]

queue = deque()
queue.append(N)
time[N] = 0


while queue:
    c = queue.popleft()

    for i in range(3):
        if i == 0:
            n_c = c - 1
        elif i == 1:
            n_c = c + 1
        else:
            n_c = 2*c

        if n_c < 0 or n_c > MAX + 1: continue
        if time[n_c] <= time[c] + 1: continue

        time[n_c] = time[c] + 1
        path_before[n_c] = c

        queue.append(n_c)
print(time[K])
res = [K]
while path_before[K] != -1:
    res.append(path_before[K])
    K = path_before[K]
print(*reversed(res))