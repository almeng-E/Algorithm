import sys
input = sys.stdin.readline
S = input().rstrip()

res = 0
for c in S:
    n = int(c)
    if n > 4:
        n -= 1
    res = res * 9 + n

print(res)