import sys
input = sys.stdin.readline
from collections import defaultdict


N, M, Q = map(int, input().split())
res = []

p = [0] * (N+1)
comps = defaultdict(set)

heavy = set()
lazy = [0] * (M+1)
offset = dict()
h_size = int(N**0.5)

for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        j, i = cmd[1:]
        # delete
        if i in comps[j]:
            # heavy 해제
            if len(comps[j]) == h_size:
                for user in comps[j]:
                    p[user] += (lazy[j] - offset[j][user])
                lazy[j] = 0
                del offset[j]
                heavy.remove(j)
            elif len(comps[j]) > h_size:
                p[i] += (lazy[j] - offset[j][i])
                del offset[j][i]
            comps[j].remove(i)

        # add
        else:
            comps[j].add(i)
            # heavy 전환
            if len(comps[j]) == h_size:
                heavy.add(j)
                if j not in offset:
                    offset[j] = dict()
                    for user in comps[j]:
                        offset[j][user] = lazy[j]
            elif len(comps[j]) > h_size:
                offset[j][i] = lazy[j]

    elif cmd[0] == 2:
        j, x = cmd[1:]
        # heavy -> lazy
        if j in heavy:
            lazy[j] += x
        else:
            for user in comps[j]:
                p[user] += x

    else:
        i = cmd[1]
        ret = p[i]
        for j in heavy:
            if i in comps[j]:
                ret += (lazy[j] - offset[j][i])
        res.append(str(ret))

print('\n'.join(res))