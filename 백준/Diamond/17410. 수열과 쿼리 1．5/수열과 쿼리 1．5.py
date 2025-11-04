import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

N = int(input())
arr = list(map(int, input().split()))

SIZE = int(N**0.5)
num_buckets = (N+SIZE-1)//SIZE
bucket = [[] for _ in range(num_buckets)]
for i in range(N):
    bucket[i//SIZE].append(arr[i])

for b in bucket:
    b.sort()

out = []

M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        i, v = cmd[1:]
        i -= 1
        bucket[i//SIZE].remove(arr[i])
        bucket[i//SIZE].append(v)
        bucket[i//SIZE].sort()
        arr[i] = v

    else:
        i, j, k = cmd[1:]
        i -= 1
        j -= 1
        cnt = 0

        lb, rb = i//SIZE, j//SIZE
        if lb == rb:
            for idx in range(i, j+1):
                if arr[idx] > k:
                    cnt += 1
        else:
            for idx in range(i, (lb+1)*SIZE):
                if arr[idx] > k:
                    cnt += 1

            for b_id in range(lb+1, rb):
                cnt += len(bucket[b_id]) - bisect_right(bucket[b_id], k)

            for idx in range(rb*SIZE, j+1):
                if arr[idx] > k:
                    cnt += 1

        out.append(str(cnt))
print('\n'.join(out))