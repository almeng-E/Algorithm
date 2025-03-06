def find_pw():
    res = 0
    for i in range(N):
        for j in range(0, M - 56 + 1):
            tmp_pw = []

            for k in range(8):
                key = board[i][j + 7 * k:j + 7 * (k + 1)]
                if key not in bit_pattern_dict.keys():
                    break
                tmp_pw.append(bit_pattern_dict[key])
            else:
                tmp_sum = 0
                for i in range(8):
                    if i % 2 == 0:
                        tmp_sum += tmp_pw[i] * 3
                    else:
                        tmp_sum += tmp_pw[i]

                if tmp_sum % 10 == 0:
                    res = sum(tmp_pw)
                    return res

    return res

bit_pattern_dict = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}

T = int(input())
for TC in range(T):
    N, M = map(int, input().split())

    board = [input() for _ in range(N)]
    res = find_pw()

    print(f'#{TC+1} {res}')