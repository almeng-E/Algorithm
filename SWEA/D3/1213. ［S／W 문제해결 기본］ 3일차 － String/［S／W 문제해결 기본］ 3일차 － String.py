
for _ in range(10):
    TC = int(input())
    pattern = input()
    text = input()

    len_p = len(pattern)
    len_t = len(text)
    i = 0   # pattern index
    j = 0   # text index

    res = 0

    while i < len_p and j < len_t:
        if pattern[i] != text[j]:
            j -= i
            i = -1
        i += 1
        j += 1

        if i == len_p:
            res += 1
            i = 0

    print(f'#{TC} {res}')