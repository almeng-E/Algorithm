import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)



N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, c = input().split()
    graph[int(u)].append((int(v), ord(c)))

t_input = input().strip()
# 상수
BASE = 37
MOD = 10**9 + 7
M = len(t_input)

# 목표 해시 (mod)
t_hash = 0
for i in range(M):
    t_hash = (t_hash + ord(t_input[i]) * pow(BASE, M-1-i, MOD)) % MOD

res = 0

def backtrack(c_node, c_hash, path):
    global res
    if len(path) >= M and c_hash == t_hash:
        res += 1

    for n_node, weight in graph[c_node]:
        # 롤링 해시 갱신 (mod)
        new_hash = (c_hash * BASE + weight) % MOD
        if len(path) >= M:
            new_hash = (new_hash - path[-M] * pow(BASE, M, MOD)) % MOD

        path.append(weight)
        backtrack(n_node, new_hash, path)
        path.pop()

backtrack(1, 0, [])
print(res)

