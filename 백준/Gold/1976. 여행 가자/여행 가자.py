import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def make_set(n):
    p = [i for i in range(n+1)]
    return p

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union_set(a, b):
    root_a = find_set(a)
    root_b = find_set(b)
    if root_a == root_b:
        return
    else:
        p[root_b] = root_a

N = int(input())
M = int(input())

p = make_set(N)

matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i):
        if matrix[i][j] == 1:
            union_set(i, j)

cities = list(map(int, input().split()))
tmp = find_set(cities[0] - 1)
for i in range(1, M):
    if tmp != find_set(cities[i] - 1):
        print('NO')
        break
else:
    print('YES')
