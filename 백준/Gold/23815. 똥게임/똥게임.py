import sys
input = sys.stdin.readline

from collections import deque


def calc(c, num):
    v = int(c[1:])
    if c[0] == '+':
        num += v
    elif c[0] == '-':
        num -= v
    elif c[0] == '*':
        num *= v
    else:
        num //= v
    return num


N = int(input())
choice = []
for _ in range(N):
    cmd = input().split()
    choice.append(cmd)
q = deque()
q.append((0, 0, 1))     # idx, jumped, num
cost = [[0, 0] for _ in range(N+1)]

while q:
    idx, jumped, num = q.popleft()
    if idx == N:
        continue
    a, b = choice[idx]
    va = calc(a, num)
    vb = calc(b, num)
    nv = max(va, vb)
    if cost[idx+1][jumped] < nv:
        cost[idx+1][jumped] = nv
        q.append((idx+1, jumped, nv))
    if not jumped and a[0] in {'-', '/'} and b[0] in {'-', '/'}:
            if cost[idx+1][1] < num:
                cost[idx+1][1] = num
                q.append((idx+1, 1, num))


res = max(cost[N])
print(res if res>0 else 'ddong game')