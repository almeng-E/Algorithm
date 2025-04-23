def find():
    res = 0
    i = 0

    while i < N:
        if a[i] == b[0]:
            for j in range(M):
                if i+j > N - 1:
                    return res
                if a[i+j] != b[j]:
                    break
            else:
                res += 1
                i += M
                continue
        i += 1
    return res

a = input(); N = len(a)
b = input(); M = len(b)


print(find())
