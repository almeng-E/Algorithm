def eat(A, B, C):
    cnt = 0
    flag = False
    if B >= C:
        diff = B-C+1
        cnt += diff
        B -= diff
        if B <= 1:
            return -1
    if A >= B:
        diff = A-B+1
        cnt += diff
        A -= diff
        if A <= 0:
            return -1
    return cnt



T = int(input())
for TC in range(T):
    A, B, C = map(int, input().split())

    res = eat(A, B, C)

    print(f'#{TC+1} {res}')