while True:
    n = int(input())
    if n == 0: break
    ret = 0
    for i in range(n+1):
        ret += i
    print(ret)