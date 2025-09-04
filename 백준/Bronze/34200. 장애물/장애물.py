N = int(input())
arr = set(map(int, input().split()))
MAX = max(arr)

cur = 0
cnt = 0
while cur < MAX:
    if cur in arr:
        cnt = -1
        break
    if cur+1 in arr:
        cur += 2
        cnt += 1
        continue
    if cur+2 in arr:
        cur += 1
        cnt += 1
        continue
    cur += 2
    cnt += 1

print(cnt)