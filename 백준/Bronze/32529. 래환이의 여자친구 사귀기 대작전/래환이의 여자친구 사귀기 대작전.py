N, M = map(int, input().split())
w = 0
d = -1
arr = list(map(int, input().split()))
for i in range(N-1, -1, -1):
    w += arr[i]
    if w >= M:
        d = i+1
        break
print(d)