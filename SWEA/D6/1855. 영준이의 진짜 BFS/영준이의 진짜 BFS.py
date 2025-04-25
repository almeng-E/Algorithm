T = int(input())
for TC in range(T):
    N = int(input())

    p = [0, 0] + list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]

    for i in range(2, N+1):
        graph[p[i]].append(i)

    for i in range(1, N+1):
        graph[i].sort()

    # depth 체크
    depth = [-1] * (N+1)
    depth[1] = 0

    queue = []
    idx = 0
    queue.append(1)

    while idx < N:
        x = queue[idx]
        idx += 1
        for nx in graph[x]:
            depth[nx] = depth[x] + 1
            queue.append(nx)

    # LCA
    def LCA(a, b):
        global res
        while depth[a] > depth[b]:
            a = p[a]
            res += 1
        while depth[a] < depth[b]:
            b = p[b]
            res += 1
        while a != b:
            a = p[a]
            b = p[b]
            res += 2
    # 거리 계산
    res = 0
    for i in range(0, N-1):
        LCA(queue[i], queue[i+1])

    print(f'#{TC+1} {res}')