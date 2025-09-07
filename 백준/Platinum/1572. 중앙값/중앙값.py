import sys
input = sys.stdin.readline 

LEN = 1 << 16
SIZE = LEN << 1

tree = [0] * SIZE

N, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
my_median = (K+1) // 2

ans = 0

# 초기 윈도우 (0 허수)
for i in range(K):
    tree[arr[i] + LEN] += 1

for i in range(LEN-1, 0, -1):
    tree[i] = tree[i<<1] + tree[(i<<1) + 1]

def slide(idx):
    add = arr[idx] + LEN
    sub = arr[idx - K] + LEN

    # tree 재구성
    while add > 0:
        tree[add] += 1
        add >>= 1

    while sub > 0:
        tree[sub] -= 1
        sub >>= 1

def find():
    global my_median, tree, ans
    X = my_median
    node = 1
    while node < LEN:
        lc = node << 1
        if tree[lc] >= X:
            node = lc
        else:
            X -= tree[lc]
            node = lc + 1
    ans += node - LEN

for i in range(K, N+1):
    slide(i)
    find()
print(ans)