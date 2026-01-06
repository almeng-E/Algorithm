p = [6,3,2,1,2]
for _ in range(2):
    a = 0
    b = list(map(int, input().split()))
    for i in range(5):
        a += p[i]*b[i]
    print(a, end=' ')