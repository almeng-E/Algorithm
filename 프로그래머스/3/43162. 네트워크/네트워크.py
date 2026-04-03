

def solution(n, computers):
    answer = 0
    
    def dfs(cur, bef):
        for nxt in range(n):
            if nxt == bef:
                continue
            if computers[cur][nxt] and not v[nxt]:
                v[nxt] = 1
                dfs(nxt, cur)
    
    v = [0] * n
    for i in range(n):
        if not v[i]:
            v[i] = 1
            dfs(i, -1)
            answer += 1
    
    return answer