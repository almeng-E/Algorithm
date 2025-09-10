N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())


tmp = 0
for sz in arr:
    if (sz % T) == 0:
        tmp += sz // T
    else:
        tmp += sz // T
        tmp += 1
print(tmp)

print(N//P, N%P)