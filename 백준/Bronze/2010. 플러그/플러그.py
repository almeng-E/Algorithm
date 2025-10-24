import sys
input = sys.stdin.readline

n = int(input())
res = 1
for _ in range(n):
    a = int(input())
    res -= 1
    res += a
print(res)