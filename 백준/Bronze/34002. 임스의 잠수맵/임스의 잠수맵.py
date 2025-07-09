
A, B, C = map(int, input().split())
S, V = map(int, input().split())
L = int(input())

goal = 250 * 100 - L * 100
res = 0
flag = True
if flag:
    for i in range(V, 0, -1):
        if goal - C*30 > 0:
            res += 30
            goal -= C*30
        else:
            res += (goal + C - 1) // C
            flag = False
            break
if flag:
    for i in range(S, 0, -1):
        if goal - B*30 > 0:
            res += 30
            goal -= B*30
        else:
            res += (goal + B - 1) // B
            flag = False
            break
if flag:
    res  += (goal + A - 1) // A
print(res)
