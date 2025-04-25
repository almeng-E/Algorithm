def solution(m, n, puddles):
    answer = 0
    MOD = 1000000007
    
    p = set()
    for i,j in puddles:
        p.add((j-1, i-1))
    
    DP = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        if (i,0) not in p:
            DP[i][0] = 1
        else:
            break
    for j in range(m):
        if (0,j) not in p:
            DP[0][j] = 1
        else:
            break
    
    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in p:
                continue
            DP[i][j] = (DP[i-1][j] + DP[i][j-1]) % MOD

    
    return (DP[n-1][m-1])%MOD