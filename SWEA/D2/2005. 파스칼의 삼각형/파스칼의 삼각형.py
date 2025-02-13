def pascal(N, cnt):
    global li
    if cnt == N:
        return

    if cnt == 0:
        tmp_list = [1]
    elif cnt == 1:
        tmp_list = [1,1]
    else:
        tmp_list = [1]
        for i in range(1, cnt):
           tmp_list.append(li[cnt-1][i-1]+li[cnt-1][i])
        tmp_list.append(1)
    li.append(tmp_list)

    return pascal(N, cnt+1)




T = int(input())
for TC in range(T):
    N = int(input())
    li = []
    pascal(N, 0)
    print(f'#{TC+1}')
    for inner in li:
        print(*inner)