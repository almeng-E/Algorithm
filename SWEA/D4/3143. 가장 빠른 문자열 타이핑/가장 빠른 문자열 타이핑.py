T = int(input())
for TC in range(T):
    A, B = input().split()
    len_text, len_pattern = len(A), len(B)

    i = 0   # text
    j = 0   # pattern

    dp = [1] * len_text

    while i < len_text and j < len_pattern:
        if A[i] != B[j]:
            i -= j
            j = -1
        i += 1
        j += 1

        if j == len_pattern: # 패턴 찾기 완료
            for k in range(len_pattern-1):
                dp[i-j+k] = 0
            j = 0


    res = sum(dp)

    print(f'#{TC+1} {res}')