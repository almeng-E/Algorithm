T = int(input())
for TC in range(1, T+1):
    N = int(input())
 
    found = 0
    cnt = 1
    while found != (1 << 10)-1:
        num = N*cnt
 
        while num:
            found = found | (1 << (num % 10))
            num //= 10
        cnt += 1
 
 
    print(f'#{TC} {(cnt-1)*N}')