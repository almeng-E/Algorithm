import sys
input = sys.stdin.readline
def check():
    for i in range(4):
        if cnt[i] >= least[i]:
            continue
        else:
            return 0
    return 1


w_idx = {'A' : 0,
       'C' : 1,
       'G' : 2,
       'T' : 3}

cnt = [0, 0, 0, 0]

P, S = map(int, input().split())
arr = input()

least = list(map(int, input().split()))

# 초기 상태
for i in range(S):
    cnt[w_idx[arr[i]]] += 1
res = 0
res += check()


for i in range(S, P):
    cnt[w_idx[arr[i]]] += 1
    cnt[w_idx[arr[i-S]]] -= 1
    res += check()
print(res)