
def find(x, y):
    global res
    if x == N - 1:
        res += 1
        return

    # 방문 처리
    v_verti[y] = True
    v_diag_up[x + y] = True
    v_diag_down[x - y] = True

    # 다음 호출 찾기
    for j in range(N):
        if not v_verti[j] and not v_diag_up[x + 1 + j] and not v_diag_down[x + 1 - j]:
            find(x + 1, j)

    # 백트래킹
    v_verti[y] = False
    v_diag_up[x + y] = False
    v_diag_down[x - y] = False


T = int(input())
for TC in range(T):
    N = int(input())

    # v_hori = [False] * N            # 인덱스 : i
    v_verti = [False] * N  # 인덱스 : j
    v_diag_up = [False] * (2 * N)  # 인덱스 : i+j
    v_diag_down = [False] * (2 * N)  # 인덱스 : i-j

    res = 0
    for j in range(N):
        find(0, j)  # i, j 인덱스

    print(f'#{TC + 1} {res}')
