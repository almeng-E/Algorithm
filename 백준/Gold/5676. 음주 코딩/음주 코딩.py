import sys
input = sys.stdin.readline

while True:
    try:
        N, K = map(int, input().split())

        arr = list(map(int, input().split()))

        LEN = 1
        while LEN < N:
            LEN <<= 1

        tree = ([1] * LEN ) + arr + ([1] * (LEN - N))
        for i in range(N):
            if arr[i] > 0:
                tree[i + LEN] = 1
            elif arr[i] == 0:
                tree[i + LEN] = 0
            else:
                tree[i + LEN] = -1

        for i in range(LEN - 1, 0, -1):
            tree[i] = tree[i * 2] * tree[i * 2 + 1]

        for _ in range(K):
            cmd, a, b = input().split()

            if cmd == 'C':
                i = int(a) + LEN - 1
                v = int(b)
                if v > 0:
                    tree[i] = 1
                elif v < 0:
                    tree[i] = -1
                else:
                    tree[i] = 0                
                i >>= 1
                while i >= 1:
                    tree[i] = tree[i * 2] * tree[i * 2 + 1]
                    i >>= 1

            else:
                i = int(a) + LEN - 1
                j = int(b) + LEN - 1

                tmp = 1
                while i <= j:
                    if i & 1:
                        tmp *= tree[i]
                        i += 1
                    if not (j & 1):
                        tmp *= tree[j]
                        j -= 1
                    i >>= 1
                    j >>= 1

                if tmp > 0:
                    print('+', end="")
                elif tmp < 0:
                    print('-', end="")
                else:
                    print('0', end="")
        print()
    except:
        break



