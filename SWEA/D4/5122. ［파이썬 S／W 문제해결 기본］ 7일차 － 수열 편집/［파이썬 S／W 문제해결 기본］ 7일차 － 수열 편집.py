T = int(input())
for TC in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = input().split()

    for _ in range(M):
        c = input().split()
        if c[0] == 'I':
            arr.insert(int(c[1]), c[2])
        elif c[0] == 'D':
            arr.pop(int(c[1]))
        else:
            arr[int(c[1])] = c[2]
    print(f'#{TC}', end=' ')
    if len(arr) >= L-1:
        print(arr[L])
    else:
        print(-1)