X, Y = map(int, input().split())
res = 0
n = 0
for i in range(X):
    n *= 10
    n += 1
res += n
n = 0
for i in range(Y):
    n *= 10
    n += 1
res += n
print(res)