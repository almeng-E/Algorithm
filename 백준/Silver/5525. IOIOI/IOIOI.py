import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()


idx = 0
res = 0
seq_cnt = 0


while idx <= M-3:
    if S[idx:idx+3] == 'IOI':
        idx += 2
        seq_cnt += 1
        if seq_cnt >= N:
            res += 1


    else:
        idx += 1
        seq_cnt = 0


print(res)

