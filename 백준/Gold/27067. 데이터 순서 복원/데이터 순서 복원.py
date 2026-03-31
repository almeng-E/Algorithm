import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = []
for i in range(N-1, -1, -1):
    if A[i] == B[i] == C[i]:
        continue
    if A[i] == B[i] and B[i] != C[i]:
        weirdo = C
        v = A[i]
    elif A[i] == C[i] and A[i] != B[i]:
        weirdo = B
        v = A[i]
    elif B[i] == C[i] and B[i] != A[i]:
        weirdo = A
        v = B[i]

    for j in range(N):
        if weirdo[j] == v:
            continue
        ans.append(weirdo[j])
        if j == i:
            ans.append(v)
    break
print(*ans)
