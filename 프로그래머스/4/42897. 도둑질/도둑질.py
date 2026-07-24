def solution(money):
    answer = 0
    n = len(money)

    # 첫 집을 터는 경우
    # dp1[i][0]: i번 집을 털지 않음
    # dp1[i][1]: i번 집을 털음
    dp1 = [[0, 0] for _ in range(n)]

    # 0번 집을 털었으므로 1번 집은 털 수 없음
    dp1[1][0] = money[0]
    dp1[1][1] = 0

    for i in range(2, n):
        dp1[i][0] = max(dp1[i - 1][0], dp1[i - 1][1])
        dp1[i][1] = money[i] + dp1[i - 1][0]

    # 첫 집을 털었으므로 마지막 집은 털지 않은 상태만 허용
    answer = max(answer, dp1[n - 1][0])

    # 첫 집을 털지 않는 경우
    dp2 = [[0, 0] for _ in range(n)]

    for i in range(1, n):
        dp2[i][0] = max(dp2[i - 1][0], dp2[i - 1][1])
        dp2[i][1] = money[i] + dp2[i - 1][0]

    answer = max(
        answer,
        dp2[n - 1][0],
        dp2[n - 1][1]
    )

    return answer