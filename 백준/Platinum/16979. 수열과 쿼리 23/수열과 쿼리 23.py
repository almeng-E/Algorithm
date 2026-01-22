import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
Q = []
for i in range(M):
    l, r = map(int, input().split())
    Q.append((l, r, i))
sqrtN = int(N**0.5)
# Q.sort(key=lambda x: (x[0]//sqrtN, x[1]))
# snake 최적화 ? zig-zag 최적화 ? 
# R 포인터 이동을 최소화하기/
Q.sort(key=lambda x: (x[0]//sqrtN, x[1] if (x[0]//sqrtN) % 2 == 0 else -x[1]))
compressed = sorted(set(arr))
v_idx_map = {v: i for i, v in enumerate(compressed)}

LEN = 1
while LEN < len(compressed):
    LEN <<= 1
SIZE = LEN << 1
tree = [0] * SIZE

ans = [0] * M
l, r = 1, 0
cnt = 0

def cnt_lt(idx):
    ret = 0
    l, r = LEN, idx-1
    while l <= r:
        if l & 1:
            ret += tree[l]
            l += 1
        if not (r & 1):
            ret += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return ret

def cnt_gt(idx):
    ret = 0
    l, r = idx+1, SIZE-1
    while l <= r:
        if l & 1:
            ret += tree[l]
            l += 1
        if not (r & 1):
            ret += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return ret

def add(idx):
    while idx:
        tree[idx] += 1
        idx >>= 1

def remove(idx):
    while idx:
        tree[idx] -= 1
        idx >>= 1

for ql, qr, qi in Q:
    while ql < l:
        l -= 1
        # 왼쪽 추가
        v = arr[l]
        idx = v_idx_map[v] + LEN
        cnt += cnt_lt(idx)
        add(idx)

    while l < ql:
        v = arr[l]
        idx = v_idx_map[v] + LEN
        cnt -= cnt_lt(idx)
        remove(idx)
        l += 1

    while qr < r:
        v = arr[r]
        idx = v_idx_map[v] + LEN
        cnt -= cnt_gt(idx)
        remove(idx)
        r -= 1

    while r < qr:
        r += 1
        v = arr[r]
        idx = v_idx_map[v] + LEN
        cnt += cnt_gt(idx)
        add(idx)

    ans[qi] = cnt

print('\n'.join(map(str, ans)))