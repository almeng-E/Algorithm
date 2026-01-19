import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())
queries = []
for i in range(M):
    l, r = map(int, input().split())
    queries.append((l, r, i))
    
sqt = int(N**0.5)
queries.sort(key=lambda x:(x[0]//sqt, x[1]))
ans = [0] * M
used = [0] * 1_000_001
cnt = 0
l, r = 1, 0

for ql, qr, i in queries:
    while r < qr:
        r += 1
        if used[arr[r]] == 0:
            cnt += 1
        used[arr[r]] += 1

    while r > qr:
        if used[arr[r]] == 1:
            cnt -= 1
        used[arr[r]] -= 1
        r -= 1

    while ql < l:
        l -= 1
        if used[arr[l]] == 0:
            cnt += 1
        used[arr[l]] += 1

    while ql > l:
        if used[arr[l]] == 1:
            cnt -= 1
        used[arr[l]] -= 1
        l += 1

    ans[i] = cnt

print('\n'.join(map(str, ans)))