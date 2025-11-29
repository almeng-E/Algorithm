import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
tmp = arr.copy()
unique = arr.copy()

queries = []
for _ in range(M):
    cmd = list(map(int, input().split()))
    queries.append(cmd)
    if cmd[0] == 1:
        i, x = cmd[1:]
        i -= 1
        tmp[i] += x
        unique.append(tmp[i])

    elif cmd[0] == 2:
        i, y = cmd[1:]
        i -= 1
        tmp[i] -= y
        unique.append(tmp[i])

    elif cmd[0] == 3:
        l, r = cmd[1:]
        unique.append(l)
        unique.append(r)

    elif cmd[0] == 4:
        t = cmd[1]

unique = sorted(set(unique))
v_to_idx = {v: i for i, v in enumerate(unique)}


def add(idx):
    while idx:
        tree[idx] += 1
        idx >>= 1


def remove(idx):
    while idx:
        tree[idx] -= 1
        idx >>= 1


def count_range(l, r):
    ret = 0
    while l <= r:
        if l % 2 == 1:
            ret += tree[l]
            l += 1
        if r % 2 == 0:
            ret += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return ret


def kth(node, s, e, k):
    if s == e:
        return s

    lc = node * 2
    rc = lc + 1
    mid = (s + e) // 2

    if tree[lc] < k:
        return kth(rc, mid+1, e, k-tree[lc])
    else:
        return kth(lc, s, mid, k)


LEN = 1
while LEN < len(unique):
    LEN <<= 1

tree = [0] * (LEN*2)

for v in arr:
    tree[v_to_idx[v] + LEN] += 1

for i in range(LEN-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2 + 1]

out = []
for cmd in queries:
    if cmd[0] == 1:
        i, x = cmd[1:]
        i -= 1
        remove(v_to_idx[arr[i]] + LEN)
        arr[i] += x
        add(v_to_idx[arr[i]] + LEN)

    elif cmd[0] == 2:
        i, y = cmd[1:]
        i -= 1
        remove(v_to_idx[arr[i]] + LEN)
        arr[i] -= y
        add(v_to_idx[arr[i]] + LEN)

    elif cmd[0] == 3:
        l, r = cmd[1:]
        out.append(str(count_range(v_to_idx[l]+LEN, v_to_idx[r]+LEN)))

    elif cmd[0] == 4:
        t = cmd[1]
        idx = kth(1, 0, LEN-1, N - t + 1)
        out.append(str(unique[idx]))


print('\n'.join(out))
