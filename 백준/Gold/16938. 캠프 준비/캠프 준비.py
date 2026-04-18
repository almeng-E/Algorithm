import sys
input = sys.stdin.readline

def backtrack(idx, c_min, c_max, c_sum):
    global ans, N, L, R, X
    if idx == N:
        if L <= c_sum <= R and c_max - c_min >= X:
            ans += 1
        return
    backtrack(idx+1, min(c_min, A[idx]), max(c_max, A[idx]), c_sum + A[idx])
    backtrack(idx+1, c_min, c_max, c_sum)


N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
backtrack(0, float('inf'), 0, 0)
print(ans)
