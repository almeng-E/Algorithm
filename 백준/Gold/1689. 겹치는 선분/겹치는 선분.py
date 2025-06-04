import sys
input = sys.stdin.readline

from collections import defaultdict
N = int(input())

lines = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    lines[a] += 1
    lines[b] -= 1

res = 0
cur = 0
inc = 0
for k in sorted(lines.keys()):
    inc += lines[k]
    res = max(res, inc)
print(res)