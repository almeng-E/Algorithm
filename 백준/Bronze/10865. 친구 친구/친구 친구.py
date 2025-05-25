import sys
input = sys.stdin.readline

N, M = map(int,input().split())
p = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    p[a] += 1
    p[b] += 1
for i in range(1, N+1):
    print(p[i])