def choose(c_idx, tmp):
    if len(tmp) == L:
        v_cnt = 0
        c_cnt = 0
        for l in tmp:
            if l in vowels:
                v_cnt += 1
            else:
                c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2:
            print(tmp)
        return

    if c_idx == C:
        return

    choose(c_idx+1, tmp + letters[c_idx])
    choose(c_idx+1, tmp)




vowels = ('a', 'e', 'i', 'o', 'u')

L, C = map(int, input().split())
letters = input().split()

letters.sort()
choose(0, '')