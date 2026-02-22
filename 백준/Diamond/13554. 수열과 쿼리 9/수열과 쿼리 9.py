import sys
input = sys.stdin.readline


def add(v, tree):
    idx = v + LEN
    while idx:
        tree[idx] += 1
        idx >>= 1


def remove(v, tree):
    idx = v + LEN
    while idx:
        tree[idx] -= 1
        idx >>= 1


def range_get(i, j, tree):
    i += LEN
    j += LEN
    ret = 0
    while i <= j:
        if i & 1:
            ret += tree[i]
            i += 1
        if not (j & 1):
            ret += tree[j]
            j -= 1
        i >>= 1
        j >>= 1
    return ret

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = int(input())
Q = []
for idx in range(M):
    i, j, k = map(int, input().split())
    Q.append((i-1, j-1, k, idx))

sqrtN = int(N**0.5)
Q.sort(key=lambda x: (x[0]//sqrtN, x[1] if (x[0] // sqrtN) % 2 == 0 else -x[1]))

LEN = 1 << 17
SIZE = LEN << 1

A_cnt = [0] * SIZE
B_cnt = [0] * SIZE

l, r = 1, 0
ans = [0] * M

for ql, qr, qk, q_idx in Q:
    while ql < l:
        l -= 1
        add(A[l], A_cnt)
        add(B[l], B_cnt)

    while l < ql:
        remove(A[l], A_cnt)
        remove(B[l], B_cnt)
        l += 1

    while r < qr:
        r += 1
        add(A[r], A_cnt)
        add(B[r], B_cnt)

    while qr < r:
        remove(A[r], A_cnt)
        remove(B[r], B_cnt)
        r -= 1

    q_ans = 0
    sqrtK = int(qk**0.5)
    for v in range(1, sqrtK+1):
        cnt_a_v = A_cnt[v+LEN]
        if cnt_a_v > 0:
            q_ans += cnt_a_v * range_get(1, qk//v, B_cnt)

        cnt_b_v = B_cnt[v+LEN]
        if cnt_b_v > 0:
            q_ans += cnt_b_v * range_get(1, qk//v, A_cnt)

    q_ans -= range_get(1, sqrtK, A_cnt) * range_get(1, sqrtK, B_cnt)
    ans[q_idx] = q_ans

print('\n'.join(map(str, ans)))