import sys

input = sys.stdin.readline

N = int(input().strip())
X = list(map(int, input().split()))

for i in range(N - 1):
    if X[i + 1] - X[i] == 1:
        print(-1)
        sys.exit(0)

ans = 0

ans += N

ans += ((X[0] - 1) + 1) // 2
for i in range(N - 1):
    d = X[i + 1] - X[i]

    if d >= 2:
        ans += ((d - 2) + 1) // 2

print(ans)