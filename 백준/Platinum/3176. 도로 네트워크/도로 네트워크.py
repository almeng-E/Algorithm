import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
graph = [[] for _ in range(N+1)]
pd = dict()
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


depth = [0] * (N+1)
parent = [-1] * (N+1)

max_depth = 0


def dfs(cur, bef, de):
    global max_depth
    depth[cur] = de
    max_depth = max(de, max_depth)
    parent[cur] = bef
    for nxt, w in graph[cur]:
        if nxt == bef:
            continue
        pd[(cur, nxt)] = w
        pd[(nxt, cur)] = w
        dfs(nxt, cur, de+1)


dfs(1, 1, 0)
pd[(1, 1)] = 0

LOG = max_depth.bit_length()
INF = float('inf')
up = [[0 for _ in range(LOG+1)] for _ in range(N+1)]
mn = [[INF for _ in range(LOG+1)] for _ in range(N+1)]
mx = [[0 for _ in range(LOG+1)] for _ in range(N+1)]

for i in range(1, N+1):
    up[i][0] = parent[i]
    mn[i][0] = pd[(i, parent[i])]
    mx[i][0] = pd[(i, parent[i])]

for j in range(1, LOG+1):
    for i in range(1, N+1):
        mid = up[i][j-1]
        up[i][j] = up[mid][j-1]
        mn[i][j] = min(mn[i][j-1], mn[mid][j-1])
        mx[i][j] = max(mx[i][j-1], mx[mid][j-1])

def LCA(x, y):
    global up
    # 무조건 x가 더 깊게 있도록
    if depth[x] < depth[y]:
        x, y = y, x

    MIN = INF
    MAX = 0

    # x를 diff 만큼 올려주자자
    diff = depth[x] - depth[y]
    for bit in range(LOG, -1, -1):
        if diff & (1 << bit):
            MIN = min(MIN, mn[x][bit])
            MAX = max(MAX, mx[x][bit])
            x = up[x][bit]

    if x == y:
        return (MIN, MAX)

    for bit in range(LOG, -1, -1):
        if up[x][bit] != up[y][bit]:
            MIN = min(MIN, mn[x][bit], mn[y][bit])
            MAX = max(MAX, mx[x][bit], mx[y][bit])
            x = up[x][bit]
            y = up[y][bit]


    MIN = min(MIN, mn[x][0], mn[y][0])
    MAX = max(MAX, mx[x][0], mx[y][0])
    return (MIN, MAX)


K = int(input())
for _ in range(K):
    d, e = map(int, input().split())
    ret = LCA(d, e)
    print(*ret)



