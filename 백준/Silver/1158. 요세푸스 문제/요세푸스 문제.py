from collections import deque

N, K = map(int, input().split())

res_arr = []

queue = deque([i for i in range(1, N+1)])

while queue:
    queue.rotate(-(K-1))
    res_arr.append(str(queue.popleft()))



print(f'<{", ".join(res_arr)}>')