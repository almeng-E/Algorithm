import sys
input = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, input().split())

arr = list(map(int, input().split()))
prv = [-1] * 1_000_001
nxt = [-1] * 1_000_001

for i in range(N):
    node = arr[i]
    ne = arr[(i + 1) % N]
    pr = arr[(i - 1 + N) % N]

    nxt[node] = ne
    prv[node] = pr

out = []

for _ in range(M):
    cmd = input().split()
    op = cmd[0]

    if op == 'BN':
        i = int(cmd[1])
        j = int(cmd[2])

        out.append(str(nxt[i]))
        nxt[j] = nxt[i]
        prv[j] = i
        prv[nxt[i]] = j
        nxt[i] = j

    elif op == 'BP':
        i = int(cmd[1])
        j = int(cmd[2])

        out.append(str(prv[i]))
        prv[j] = prv[i]
        nxt[j] = i
        nxt[prv[i]] = j
        prv[i] = j

    elif op == 'CN':
        i = int(cmd[1])

        out.append(str(nxt[i]))
        nxt[i] = nxt[nxt[i]]
        prv[nxt[i]] = i

    elif op == 'CP':
        i = int(cmd[1])

        out.append(str(prv[i]))
        prv[i] = prv[prv[i]]
        nxt[prv[i]] = i

write("\n".join(out))
