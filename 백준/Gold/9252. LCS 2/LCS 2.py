import sys
input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()

DP = [[0 for _ in range(len(S2) + 1)] for _ in range(len(S1) + 1)]
bef = [[(0, 0) for _ in range(len(S2) + 1)] for _ in range(len(S1) + 1)]
for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            DP[i+1][j+1] = DP[i][j] + 1
            bef[i+1][j+1] = (i, j)

        else:
            if DP[i][j+1] < DP[i+1][j]:
                DP[i+1][j+1] = DP[i+1][j]
                bef[i+1][j+1] = (i+1, j)
            else:
                DP[i+1][j+1] = DP[i][j+1]
                bef[i+1][j+1] = (i, j+1)


i, j = len(S1), len(S2)
ans = []
while i > 0 and j > 0:
    if S1[i-1] == S2[j-1]:
        ans.append(S1[i-1])
    i, j = bef[i][j]

print(DP[-1][-1])
if DP[-1][-1] > 0:
    print(''.join(reversed(ans)))