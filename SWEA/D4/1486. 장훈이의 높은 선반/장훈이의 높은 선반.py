def dfs(c_idx, tmp_sum):
    global res
    if tmp_sum < B:
        return
    if c_idx == N:
        res = min(res, tmp_sum-B)
        return


    dfs(c_idx+1, tmp_sum)
    tmp_sum -= HEIGHTS[c_idx]
    dfs(c_idx+1, tmp_sum)




T = int(input())

for TC in range(T):
    N, B = map(int, input().split())
    HEIGHTS = list(map(int, input().split()))

    res = B
    dfs(0, sum(HEIGHTS))

    print(f'#{TC+1} {res}')