import sys
input = sys.stdin.readline
M, N = map(int, input().split())
T = int(input())
garo = [0, N]
sero = [0, M]
for _ in range(T):
    a, b = map(int, input().split())
    if a == 0:
        garo.append(b)
    else:
        sero.append(b)
garo.sort()
sero.sort()
res = 0
for i in range(len(garo) - 1):
    for j in range(len(sero) - 1):
        tmp = (garo[i + 1] - garo[i]) * (sero[j + 1] - sero[j])
        if res < tmp:
            res = tmp
print(res)


