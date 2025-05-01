def backtrack(sour, bitter, c_idx):
    global res
    if c_idx == N:
        if sour==1 and bitter==0:
            return
        res = min(res, abs(sour - bitter))
        return

    backtrack(sour, bitter, c_idx+1)
    backtrack(sour*ing[c_idx][0], bitter+ing[c_idx][1], c_idx+1)


    pass
N = int(input())
res = float('inf')

ing = [tuple(map(int, input().split())) for _ in range(N)]

backtrack(1, 0, 0)

print(res)