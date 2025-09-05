import sys
input = sys.stdin.readline

N = int(input())

parts_cnt = dict()
p = dict()


def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return p[x]

def union(a, b):
    rt_a = find(a)
    rt_b = find(b)
    sz_a = parts_cnt[rt_a]
    sz_b = parts_cnt[rt_b]
    if rt_a != rt_b:
        if sz_a < sz_b:
            p[rt_a] = rt_b
            parts_cnt[rt_b] += sz_a
        else:
            p[rt_b] = rt_a
            parts_cnt[rt_a] += sz_b


for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'I':
        a, b = map(int, cmd[1:])

        if a not in p:
            p[a] = a
            parts_cnt[a] = 1
        if b not in p:
            p[b] = b
            parts_cnt[b] = 1

        union(a, b)

    else:
        c = int(cmd[1])
        if c not in p:
            p[c] = c
            parts_cnt[c] = 1

        r_idx = find(c)
        print(parts_cnt[r_idx])