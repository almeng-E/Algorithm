import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    rta = find(a)
    rtb = find(b)
    if rta != rtb:
        p[rta] = rtb


N, Q = map(int, input().split())

# 원본
original_p = [i for i in range(N+1)]
for i in range(2, N+1):
    original_p[i] = int(input())


p = [i for i in range(N+1)]
queries = []
for _ in range(N-1+Q):
    queries.append(input().rstrip())
out = []

queries.reverse()
for q in queries:
    cmd = list(map(int, q.split()))
    if cmd[0] == 0:
        a = cmd[1]
        union(a, original_p[a])

    else:
        a, b = cmd[1], cmd[2]
        if find(a) == find(b):
            out.append('YES')
        else:
            out.append('NO')

out.reverse()
for o in out:
    print(o)