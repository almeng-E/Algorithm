import sys
input = sys.stdin.readline
while True:
    N, K = map(int, input().split())
    if N == 0:
        break

    arr = list(map(int, input().split()))
    if K == arr[0]:
        print(0)
        continue

    parent = [-1] * N                    # idx
    # depth = [0] * N
    children = [[] for _ in range(N)]   # index

    nextP = 0                           # index
    for i in range(1, N):
        if arr[i] == K:
            t = i

        if arr[i] - arr[i-1] > 1:
            p = nextP
            nextP += 1
            parent[i] = p
            children[p].append(i)
            # depth[i] = depth[p] + 1

        elif arr[i] - arr[i-1] == 1:
            p = parent[i-1]
            parent[i] = p
            children[p].append(i)
            # depth[i] = depth[p] + 1


    p = parent[t]
    if p == -1:
        print(0)
        continue
    pp = parent[p]
    if pp == -1:
        print(0)
        continue
    res = 0
    for c in children[pp]:
        if c == p:
            continue

        res += len(children[c])

    print(res)
