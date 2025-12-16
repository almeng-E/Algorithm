import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[a].append(c)

v_cnt = 0
res = 0
r_check_cnt = 0
def dfs(cur):
    global v_cnt, res, r_check_cnt
    v_cnt += 1

    lc, rc = graph[cur]
    if lc != -1:
        res += 1
        dfs(lc)
        res += 1
    r_check_cnt += 1
    if rc != -1:
        res += 1
        dfs(rc)

        if v_cnt == N and r_check_cnt == N:
            return
        res += 1


dfs(1)
print(res)
