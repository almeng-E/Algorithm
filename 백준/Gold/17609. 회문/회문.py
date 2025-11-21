import sys
input = sys.stdin.readline

def check(S, l, r):
    isChanged = False
    while l <= r:
        if S[l] == S[r]:
            l += 1
            r -= 1
            continue
        else:
            if not isChanged:
                rr = check2(S, l, r-1)
                ll = check2(S, l+1, r)
                if rr != 2 or ll != 2:
                    return 1
                else:
                    return 2
    return 0


def check2(S, l, r):
    while l <= r:
        if S[l] == S[r]:
            l += 1
            r -= 1
            continue
        else:
            return 2
    return 0


T = int(input())
for _ in range(T):
    S = input().rstrip()
    ret = check(S, 0, len(S)-1)
    print(ret)