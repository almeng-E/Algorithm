N = int(input())
arr = list(map(int,input().split()))
if N == 1:
    print(sum(arr) - max(arr))
else:
    ml = []
    ml.append(min(arr[0], arr[5]))
    ml.append(min(arr[1], arr[4]))
    ml.append(min(arr[2], arr[3]))

    ml.sort()

    min1 = ml[0]
    min2 = ml[0] + ml[1]
    min3 = ml[0] + ml[1] + ml[2]

    cnt1 = 4 * (N - 1) * (N - 2) + (N - 2) ** 2
    cnt2 = 4 * (N - 1) + 4 * (N - 2)
    cnt3 = 4

    ans = (cnt1 * min1) + (cnt2 * min2) + (cnt3 * min3)
    print(ans)