for TC in range(10):
    N = int(input())
    res = sum(map(int, input().split('+')))
    print(f'#{TC+1} {res}')