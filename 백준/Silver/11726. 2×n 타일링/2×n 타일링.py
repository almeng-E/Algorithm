import sys
n=int(sys.stdin.readline().rstrip())



def tile(n):
    dp=[0] * (n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-2] +dp[i-1])%10007
    return dp[n]
print(tile(n) if n>=3 else(1 if n==1 else 2))
        
