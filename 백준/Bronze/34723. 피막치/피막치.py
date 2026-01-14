import sys
input = sys.stdin.readline

P, M, C = map(int, input().split())
X = int(input())
res = float('inf')

for p in range(1, P+1):
    for m in range(1, M+1):
        for c in range(1, C+1):
            res = min(res, abs((p+m)*(m+c) - X))
print(res)