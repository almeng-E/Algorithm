def find_subset(c_index, tmp_subset):
    global A, result
    # 가지치기
    if sum(tmp_subset) > K:
        return
    elif sum(tmp_subset) == K:
        result += 1
        return

    # base-case
    if c_index == N:
        return


    # 현재 요소를 포함하지 않고 넘기기
    find_subset(c_index+1, tmp_subset)

    # 현재 요소를 포함하고 넘기기
    tmp_subset.append(A[c_index])
    find_subset(c_index+1, tmp_subset)
    # 원상복구 백트래킹
    tmp_subset.pop()




T = int(input())
for TC in range(T):
    N, K = map(int, input().split())

    A = list(map(int, input().split()))

    result = 0
    find_subset(0, [])

    print(f'#{TC+1} {result}')