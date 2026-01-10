import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
cnt = 0
while N >= 2 and M >= 1 and N+M >= K+3:
    cnt += 1
    N -= 2
    M -= 1
print(cnt)