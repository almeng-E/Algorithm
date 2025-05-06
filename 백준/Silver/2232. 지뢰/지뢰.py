N = int(input())
arr = [int(input()) for _ in range(N)]
p = [-1 for _ in range(N)]
if N == 1:
    print(1)
else:
    for i in range(N):
        if i == 0:
            if arr[i] < arr[i+1]:
                p[i] = i+1
        elif i == N-1:
            if arr[i-1] > arr[i]:
                p[i] = i-1
        else:
            if arr[i] < arr[i+1]:
                p[i] = i+1
            elif arr[i-1] > arr[i]:
                p[i] = i-1
    for i in range(N):
        if p[i] == -1:
            print(i+1)
