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
    par = [0] * (V+1)
    size = [1] * (V+1)
    dfs(1, 0)

    # sparce table을 채워보자
    LOG = V.bit_length()

    up = [[0 for _ in range(LOG)] for _ in range(V+1)]
    # 직접 부모
    for i in range(1, V+1):
        up[i][0] = par[i]

    # 나머지 sparce table 채우기
    for j in range(1, LOG):
        for i in range(1, V+1):
            up[i][j] = up[ up[i][j-1] ][ j-1 ]
            # mid = up[i][j-1]
            # up[i][j] = up[mid][j-1]

    # LCA - binary lifting
    # A가 더 깊음
    if depth[A] < depth[B]:
        A, B = B, A
    diff = depth[A] - depth[B]
    # 2진수 분해 점프
    for k in range(LOG-1, -1, -1):
        if diff & (1 << k):
            A = up[A][k]

    if A != B:
        for i in range(LOG-1, -1, -1):
            if up[A][i] != up[B][i]:
                A = up[A][i]
                B = up[B][i]
        A = par[A]

    print(f'#{TC+1} {A} {size[A]}')