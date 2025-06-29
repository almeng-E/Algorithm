N = int(input())

weights = list(map(int, input().split()))
weights.sort()

res = 1
for w in weights:
    if res < w:
        break
    else:
        res += w
print(res)