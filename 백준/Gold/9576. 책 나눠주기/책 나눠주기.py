import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())

    arr = []
    for _ in range(M):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: (x[1], x[0]))


    res = 0

    for cur_max in range(N, 0, -1):
        tmp = []
        # 안되는것 커트
        while arr and arr[-1][1] > cur_max:
            x = arr.pop()
            if x[0] > cur_max:
                continue
            x[1] = cur_max
            tmp.append(x)
        arr.extend(tmp)
        arr.sort(key=lambda x: (x[1], x[0]))

        if not arr:
            break

        if arr[-1][0] <= cur_max <= arr[-1][1]:
            res += 1
            arr.pop()

    print(res)