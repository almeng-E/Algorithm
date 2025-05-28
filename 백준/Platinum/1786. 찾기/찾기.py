import sys
input = sys.stdin.readline



# 라빈 카프

BASE = 97
MOD = 10**9 + 7

T = input().rstrip()
P = input().rstrip()
n, m = len(T), len(P)

if n < m:
    print(0)
else:
    # KEY 만들기
    KEY = 0
    for c in P:
        KEY = (KEY*BASE + ord(c)) % MOD
    
    # window
    window = 0
    for i in range(m):
        window = (window*BASE + ord(T[i])) % MOD
    
    res = 0
    idx = []
    
    if window == KEY:
        res += 1
        idx.append(1)
    
    high = pow(BASE, m-1, MOD)
    
    # sliding window
    for i in range(m, n):
        window = (window - ord(T[i-m]) * high) % MOD
        window = (window * BASE) % MOD
        window = (window + ord(T[i]))
    
        if window == KEY:
            res += 1
            idx.append(i-m+2)
    print(res)
    print(*idx)
