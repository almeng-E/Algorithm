def change_and_find_pointer():
    j = 0
    while True:
        for i in range(8):
            tmp = pw[i] - sub[j] 
            j += 1
            # 순환
            if j == 5:
                j = 0
 
            if tmp <= 0:
                pw[i] = 0
                return i
            else:
                pw[i] = tmp
 
sub = (1, 2, 3, 4, 5)
 
for _ in range(10):
    TC = int(input())
    pw = list(map(int, input().split()))
 
    base_index = change_and_find_pointer()
 
    res = []
 
    for i in range(base_index, 8):
        res.append(pw[i])
    for i in range(0, base_index):
        res.append(pw[i])
 
    print(f'#{TC}', *res[1:], res[0])