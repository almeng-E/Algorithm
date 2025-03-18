def find(depth, tmp, l_idx):
    global res
    if depth >= N:
        return

    if tmp == K:
        res += 1
        return

    for i in range(l_idx, N):
        if not visited[i]:
            visited[i] = True
            find(depth+1, tmp + arr[i], i+1)
            visited[i] = False


T = int(input())
for TC in range(T):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))

    res = 0

    visited = [False] * N


    find(0, 0, 0)

    print(f'#{TC+1} {res}')