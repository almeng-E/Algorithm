N, score, P = map(int, input().split())
if N:
    arr = list(map(int, input().split()))
    if len(arr)+1 <= P:
        arr.append(score)
        arr.sort(reverse=True)
        print(arr.index(score)+1)
    else:
        if arr[-1] >= score:
            print(-1)
        else:
            arr.append(score)
            arr.sort(reverse=True)
            print(arr.index(score)+1)
else:
    print(1)