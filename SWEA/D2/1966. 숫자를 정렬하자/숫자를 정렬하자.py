def find_max(iterable):
    tmp = iterable[0]
    for i in iterable:
        if tmp < i:
            tmp = i
    return tmp
 
 
t = int(input())
for tc in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    counter = [0] * (find_max(li)+1)
    for i in li:
        counter[i] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    res = [0] * n
    for i in range(len(li)-1, -1, -1):
        counter[li[i]] -= 1
        res[counter[li[i]]] = li[i]
    print(f'#{tc+1} ', end="")
    print(*res)