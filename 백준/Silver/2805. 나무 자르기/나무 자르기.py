from collections import Counter

N, M = map(int, input().split())
trees = list(map(int, input().split()))

counted = Counter(trees)


bottom = 0
top = 1000000000

res = 0

while bottom <= top:
    middle = (bottom + top)//2

    # middle 체크
    tmp = 0
    # for h in trees:
    #     if h >= middle:
    #         tmp += h-middle
    for height, cnt in counted.items():
        if height >= middle:
            tmp += (height-middle) * cnt

    if tmp >= M:
        res = max(res, middle)
        bottom = middle + 1
    else:
        top = middle - 1

print(res)