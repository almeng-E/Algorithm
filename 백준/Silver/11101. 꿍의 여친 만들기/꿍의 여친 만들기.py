T = int(input())
for _ in range(T):
    a = input().split(',')
    b = input().split('|')

    for i in range(len(a)):
        c, d = a[i].split(':')
        a[i] = (c, int(d))

    for i in range(len(b)):
        c = b[i].split('&')
        b[i] = set(c)

    time = [0] * len(b)


    for k, v in a:
        for j in range(len(b)):
            if k in b[j]:
                time[j] = max(time[j], v)
                b[j].remove(k)

    print(min(time))