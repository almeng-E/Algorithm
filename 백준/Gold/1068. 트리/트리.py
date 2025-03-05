import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v):
    global res

    if visited[v]:
        return
    visited[v] = True
    is_leaf = True  # 우선 이 노드를 리프라고 가정

    for next_node in graph[v]:
        if not visited[next_node]:
            is_leaf = False
            dfs(next_node)
    if is_leaf:
        res += 1

N = int(input())

graph = [[] for _ in range(N)]
res_tree = [0] * N
li = list(map(int, input().split()))

roots = []

for i in range(N):
    if li[i] != -1:
        graph[li[i]].append(i)
    else:
        roots.append(i)

K = int(input())

res = 0

for root in roots:
    visited = [False] * N
    visited[K] = True

    dfs(root)

print(res)