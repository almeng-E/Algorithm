t = int(input())
 
for tc in range(t):
    res = 0
    for i in map(int, input().split()):
        if i%2 == 1:
            res += i
    print(f'#{tc+1} {res}')