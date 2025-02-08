white = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for _ in range(n):
    x1, y1 = map(int, input().split())
    x1-=1
    y1-=1
    for i in range(x1, x1+10):
        for j in range(y1, y1+10):
            if white[i][j] == 0:
                white[i][j] = 1
            else:
                continue
res = 0
for i in white:
    res += sum(i)

print(res)