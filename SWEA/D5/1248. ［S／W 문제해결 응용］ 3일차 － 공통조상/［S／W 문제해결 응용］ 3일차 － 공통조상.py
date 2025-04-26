def dfs(cur, prv):
    for nxt in graph[cur]:
        if nxt != prv:
            par[nxt] = cur
            depth[nxt] = depth[cur] + 1
            dfs(nxt, cur)
            size[cur] += size[nxt]



T = int(input())
for TC in range(T):
    V, E, A, B = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    arr = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        graph[arr[i]].append(arr[i+1])

    depth = [0] * (V+1)
    par = [1] * (V+1)
    size = [1] * (V+1)

    dfs(1, 1)
    while depth[A] > depth[B]:
        A = par[A]
    while depth[A] < depth[B]:
        B = par[B]
    while A != B:
        A = par[A]
        B = par[B]
    print(f'#{TC+1} {A} {size[A]}')