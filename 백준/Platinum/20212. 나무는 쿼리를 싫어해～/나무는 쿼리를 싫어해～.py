import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def push_down(node, s, e):
    if not lazy[node]:
        return

    tree[node] += lazy[node] * width[node]
    if s != e:
        lc = node << 1
        rc = lc + 1
        lazy[lc] += lazy[node]
        lazy[rc] += lazy[node]
    lazy[node] = 0


def range_update(node, s, e, ts, te, v):
    push_down(node, s, e)

    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        lazy[node] += v
        push_down(node, s, e)
        return

    lc = node << 1
    rc = lc + 1
    mid = (s + e) >> 1
    range_update(lc, s, mid, ts, te, v)
    range_update(rc, mid+1, e, ts, te, v)

    tree[node] = tree[lc] + tree[rc]


def range_get(node, s, e, ts, te):
    global tmp
    push_down(node, s, e)

    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        tmp += tree[node]
        return

    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1
    range_get(lc, s, mid, ts, te)
    range_get(rc, mid+1, e, ts, te)


M = int(input())
Q1 = []
Q2s = dict()
q2idx = 0
coords = []

for _ in range(M):
    cmd, i, j, k = map(int, input().split())
    if cmd == 1:
        Q1.append((i, j, k))
    else:
        if k-1 in Q2s:
            Q2s[k-1].append((q2idx, i, j))
        else:
            Q2s[k-1] = [(q2idx, i, j)]
        q2idx += 1
    # 범위를 하나의 노드로 [i, j+1)
    coords.append(i)
    coords.append(j+1)

# 압축
coords = sorted(set(coords))
compressed = dict()
for i, v in enumerate(coords):
    compressed[v] = i


# 트리 생성
N = len(coords) -1
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
width = [0] * SIZE
lazy = [0] * SIZE

for i in range(N):
    width[i + LEN] = coords[i+1] - coords[i]
for i in range(LEN-1, 0, -1):
    width[i] = width[i*2] + width[i*2 + 1]

# 결과
ans_list = [0] * q2idx
for x in range(len(Q1)):
    i, j, k = Q1[x]
    l, r = compressed[i], compressed[j+1]-1
    range_update(1, 0, LEN-1, l, r, k)
    if x in Q2s:
        for idx, a, b in Q2s[x]:
            tmp = 0
            range_get(1, 0, LEN-1, compressed[a], compressed[b+1]-1)
            ans_list[idx] = tmp

print('\n'.join(map(str, ans_list)))
# 아오어려워