import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input())
arr = list(map(int, input().split()))
SIZE = int(N**0.5)
num_buckets = (N+SIZE-1) // SIZE

buckets = [[] for _ in range(num_buckets)]
for i in range(N):
    b_idx = i//SIZE
    buckets[b_idx].append(arr[i])

for b in buckets:
    b.sort()
out = []
M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        i, j, k = cmd[1:]
        i -= 1
        j -= 1
        lb = i//SIZE
        rb = j//SIZE
        cnt = 0
        if lb == rb:
            # 직접 탐색 왼 버킷
            for idx in range(i, j+1):
                if arr[idx] > k:
                    cnt += 1
        else:
            # 직접 탐색 왼 버킷
            for idx in range(i, (lb+1)*SIZE):
                if arr[idx] > k:
                    cnt += 1

            # 포함 버킷
            for b_idx in range(lb+1, rb):
                cnt += len(buckets[b_idx]) - bisect_right(buckets[b_idx], k)

            for idx in range(rb*SIZE, j+1):
                if arr[idx] > k:
                    cnt += 1
        out.append(str(cnt))
    else:
        i, k = cmd[1:]
        i -= 1
        buckets[i//SIZE].remove(arr[i])
        buckets[i//SIZE].append(k)
        buckets[i//SIZE].sort()
        arr[i] = k
print('\n'.join(out))
