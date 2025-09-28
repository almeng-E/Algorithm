import sys
input = sys.stdin.readline

d = dict()

N = int(input())

for _ in range(N):
    a, b = input().split()
    if a not in d:
        d[a] = 0
    if b not in d:
        d[b] = 0

    if a == "ChongChong":
        d[a] = 1
    if b == "ChongChong":
        d[b] = 1

    if d[a] or d[b]:
        d[a] = 1
        d[b] = 1

print(sum(d.values()))