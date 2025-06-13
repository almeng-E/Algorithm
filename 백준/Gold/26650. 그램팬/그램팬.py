import sys
input = sys.stdin.readline


def main():
    S = input().rstrip()
    n = len(S)
    res = 0
    st = 0
    while st < n:
        if S[st] != 'A':
            st += 1
            continue

        ed = st
        a_cnt = 0
        z_cnt = 0
        prev = chr(64)

        while ed < n:
            curr = S[ed]
            if ord(curr) - ord(prev) not in (0, 1):
                break

            if S[ed] == 'A':
                a_cnt += 1
            elif S[ed] == 'Z':
                z_cnt += 1

            prev = curr
            ed += 1

        if a_cnt > 0 and z_cnt > 0:
            res += a_cnt * z_cnt
        
        # 점프
        st = ed

    print(res)
main()