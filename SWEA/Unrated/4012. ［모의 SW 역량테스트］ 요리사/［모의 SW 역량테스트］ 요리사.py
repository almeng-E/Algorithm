def make_comb(c_idx):
    global res
    if len(tmp_set) == N//2:
        res = min(res, find_answer(tmp_set))
        return

    if c_idx == N:
        return

    make_comb(c_idx + 1)
    tmp_set.add(c_idx)
    make_comb(c_idx+1)
    tmp_set.remove(c_idx)





def find_answer(a_set):
    a_taste = 0
    b_taste = 0
    b_set = list(full_set - a_set)
    a_set = list(a_set)
    for i in range(N//2):
        for j in range(i+1, N//2):
            a_taste += board[a_set[i]][a_set[j]] + board[a_set[j]][a_set[i]]
            b_taste += board[b_set[i]][b_set[j]] + board[b_set[j]][b_set[i]]

    return abs(a_taste - b_taste)




T = int(input())
for TC in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    res = float('inf')

    full_set = set(i for i in range(N))
    tmp_set = set()
    make_comb(0)

    print(f'#{TC+1} {res}')