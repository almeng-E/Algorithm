import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

DP = [[0, 0] for _ in range(N+1)]
stack = [(1, 0, 1)]   # (현재 노드, 부모 노드, 진입 여부)

while stack:
    cur, bef, go_in = stack.pop()
    if go_in:  # 진입
        stack.append((cur, bef, 0))  # 진출 예약
        for nxt in graph[cur]:
            if nxt != bef:
                stack.append((nxt, cur, 1))
    else:  # 진출
        DP[cur][0] = 0
        DP[cur][1] = 1
        for nxt in graph[cur]:
            if nxt == bef:
                continue
            DP[cur][0] += DP[nxt][1]
            DP[cur][1] += min(DP[nxt][0], DP[nxt][1])

print(min(DP[1]))