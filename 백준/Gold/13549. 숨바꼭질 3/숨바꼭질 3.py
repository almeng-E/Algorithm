from collections import deque
N, K = map(int, input().split())

INF = 1e9
MAX = max(N, K) * 2


memo = [INF] * (MAX + 1)

queue = deque()
queue.append((N, 0))

while queue:
    c_num, cnt = queue.popleft()
    if c_num < 0 or c_num > MAX:
        continue

    if memo[c_num] <= cnt:
        continue

    memo[c_num] = cnt


    queue.append((c_num*2, cnt))
    queue.append((c_num+1, cnt+1))
    queue.append((c_num-1, cnt+1))

print(memo[K])