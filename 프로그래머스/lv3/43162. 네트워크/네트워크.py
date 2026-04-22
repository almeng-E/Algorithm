def dfs(cur, bef):
    global n
    for nxt in range(n):
        if nxt == bef:
            continue
        if computers[cur][nxt] and not v[nxt]:
            v[nxt] = 1
            dfs(nxt, cur)

def solution(n, computers):
    global n
    answer = 0
    v = [0] * n
    for i in range(n):
        if not v[i]:
            v[i] = 1
            dfs(i, -1)
            answer += 1
    
    return answer