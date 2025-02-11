
T = int(input())
for TC in range(T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        for k in range(i, i+j-1):
            if k < N:
                li[k] = li[i-1]


    print(f'#{TC+1} ', end="")
    print(*li)