import sys
input = sys.stdin.readline


N = int(input())
LEN = 1 << 21
SIZE = LEN << 1

ans = []
tree = [0] * SIZE

for _ in range(N):
    T, X = map(int, input().split())
    if T == 1:
        X += LEN
        while X >= 1:
            tree[X] += 1
            X >>= 1

    else:
        # k번째 원소 찾기
        node = 1
        while node < LEN:
            lc = node << 1
            if tree[lc] >= X:
                node = lc
            else:
                X -= tree[lc]
                node = lc + 1

        ans.append(str(node - LEN))

        while node > 0:
            tree[node] -= 1
            node >>= 1

sys.stdout.write('\n'.join(ans))