import sys
input = sys.stdin.readline
def solve():
    ret = []
    N, Q = map(int, input().split())
    S = [set() for _ in range(N+1)]
    for i in range(1, N+1):
        _, *arr = map(int, input().split())
        S[i] = set(arr)

    for _ in range(Q):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            a, b = cmd[1:]
            if len(S[a]) < len(S[b]):
                S[a], S[b] = S[b], S[a]
            S[a] |= S[b]
            S[b].clear()
        else:
            a = cmd[1]
            ret.append(str(len(S[a])))
    print('\n'.join(ret))
solve()