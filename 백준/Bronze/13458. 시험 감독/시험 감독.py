N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

res = 0
for i in range(N):
    tmp = A[i]
    res += 1
    tmp -= B
    if tmp <= 0:
        continue
    if tmp%C == 0:
        res += tmp//C
    else:
        res += (tmp//C)+1
print(res)