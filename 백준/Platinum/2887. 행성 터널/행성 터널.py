import sys
input = sys.stdin.readline

def solve():
    def get_edge(axis):
        axis.sort()
        for i in range(N-1):
            edges.append((abs(axis[i+1][0] - axis[i][0]), axis[i+1][1], axis[i][1]))


    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]


    def union(a, b):
        rt_a = find(a)
        rt_b = find(b)
        if rt_a != rt_b:
            if sz[rt_b] > sz[rt_a]:
                p[rt_a] = rt_b
            else:
                p[rt_b] = p[rt_a]
            return 1
        else:
            return 0


    N = int(input())

    X = []
    Y = []
    Z = []
    for i in range(N):
        pos = map(int, input().split())
        X.append((next(pos), i))
        Y.append((next(pos), i))
        Z.append((next(pos), i))

    edges = []
    get_edge(X)
    get_edge(Y)
    get_edge(Z)

    edges.sort()

    p = [i for i in range(N)]
    sz = [1 for _ in range(N)]
    cnt = 0
    ans = 0

    for cost, a, b in edges:
        if union(a, b):
            ans += cost
            cnt += 1

        if cnt == N-1:
            break

    print(ans)
solve()
