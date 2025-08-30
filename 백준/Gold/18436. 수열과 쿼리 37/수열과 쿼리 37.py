import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

LEN = 1
while LEN < N:
    LEN <<= 1
SiZE = LEN << 1

odd = [0] * SiZE
even = [0] * SiZE

for i in range(N):
    if arr[i] & 1:
        odd[i+LEN] = 1
    else:
        even[i+LEN] = 1

for i in range(LEN-1, 0, -1):
    odd[i] = odd[i*2] + odd[i*2 + 1]
    even[i] = even[i*2] + even[i*2 + 1]

M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        idx, x = cmd[1] + LEN - 1, cmd[2]
        if even[idx] and x & 1:
            c = idx
            even[c] = 0
            c >>= 1
            while c:
                even[c] -= 1
                c >>= 1
            odd[idx] = 1
            idx >>= 1
            while idx:
                odd[idx] += 1
                idx >>= 1
        elif odd[idx] and not x & 1:
            c = idx
            odd[c] = 0
            c >>= 1
            while c:
                odd[c] -= 1
                c >>= 1
            even[idx] = 1
            idx >>= 1
            while idx:
                even[idx] += 1
                idx >>= 1
        continue
    elif cmd[0] == 2:
        tree = even
    else:
        tree = odd

    l, r = cmd[1] + LEN - 1, cmd[2] + LEN - 1
    cnt = 0
    while l <= r:
        if l & 1:
            cnt += tree[l]
            l += 1
        if not r & 1:
            cnt += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    print(cnt)