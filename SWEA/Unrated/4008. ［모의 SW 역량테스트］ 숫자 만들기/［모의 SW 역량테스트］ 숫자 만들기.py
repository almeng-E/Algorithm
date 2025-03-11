def recur(num_idx, tmp_res):
    global max_res, min_res
    if num_idx == N-1:
        # print(tmp_res)
        max_res = max(max_res, tmp_res)
        min_res = min(min_res, tmp_res)


    for i in range(4):
        if op_cnt[i] == 0:
            continue
        else:
            op_cnt[i] -= 1
            if i == 0:
                recur(num_idx+1, tmp_res + cards[num_idx])
            elif i == 1:
                recur(num_idx+1, tmp_res - cards[num_idx])
            elif i == 2:
                recur(num_idx+1, tmp_res * cards[num_idx])
            else:
                recur(num_idx+1, int(tmp_res / cards[num_idx]))
            op_cnt[i] += 1



T = int(input())

for TC in range(T):
    N = int(input())
    # 0 : +, 1 : -, 2 : *, 3 : /
    op_cnt = list(map(int, input().split()))

    first_num, *cards = map(int, input().split())

    max_res = -float('inf')
    min_res = float('inf')

    recur(0, first_num)

    print(f'#{TC+1} {max_res - min_res}')