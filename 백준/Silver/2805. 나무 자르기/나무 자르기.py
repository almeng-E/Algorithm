N, M = map(int, input().split())
trees = list(map(int, input().split()))

bottom = 0
top = 1000000000

res = 0

while bottom <= top:
    middle = (bottom + top)//2

    # middle 체크
    tmp = 0
    for h in trees:
        if h >= middle:
            tmp += h-middle
    if tmp >= M:
        res = max(res, middle)
        bottom = middle + 1
    else:
        top = middle - 1

print(res)