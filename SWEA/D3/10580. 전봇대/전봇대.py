T = int(input())
for TC in range(T):
    a_pole = []
    b_pole = []
    N = int(input())
    res = 0
    for _ in range(N):
        A, B = map(int, input().split())
        a_pole.append(A)
        b_pole.append(B)
    for i in range(N):
        for j in range(i, N):
            if (a_pole[i] > a_pole[j] and b_pole[i] < b_pole[j]) or (a_pole[i] < a_pole[j] and b_pole[i] > b_pole[j]):
                res += 1

    print(f'#{TC+1} {res}')
