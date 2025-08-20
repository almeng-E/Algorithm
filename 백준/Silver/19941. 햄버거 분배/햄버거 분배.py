import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
used = [False] * N
arr = input().rstrip()

for i in range(N):
    if used[i]:
        continue
    used[i] = True
    if arr[i] == 'P':
        for j in range(i + 1, i + K + 1):
            if j >= N:
                break
            if used[j]:
                continue
            if arr[j] == 'H':
                used[j] = True
                cnt += 1
                break

    else:
        for j in range(i + 1, i + K + 1):
            if j >= N:
                break
            if used[j]:
                continue
            if arr[j] == 'P':
                used[j] = True
                cnt += 1
                break
print(cnt)