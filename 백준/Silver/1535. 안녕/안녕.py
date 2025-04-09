
N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
DP = [0] * 101
li = list(zip(L, J))


for l, j in li:
    for i in range(100, l, -1):
        DP[i] = max(DP[i], DP[i-l]+j)
print(DP[100])
