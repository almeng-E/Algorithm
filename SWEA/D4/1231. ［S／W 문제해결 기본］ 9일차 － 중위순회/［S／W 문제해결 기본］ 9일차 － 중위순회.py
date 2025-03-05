def in_order(v):

    if tree[v] == 0:
        return

    # 왼쪽 자식
    if left[v]:
        in_order(left[v])
    # 자신 호출
    print(tree[v], end="")
    # 오른쪽 자식 호출
    if right[v]:
        in_order(right[v])





for TC in range(10):
    N = int(input())

    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    # 정점 정보 입력
    for _ in range(N):
        a, b, *c = input().split()
        tree[int(a)] = b
        if len(c) >= 1:
            left[int(a)] = int(c[0])
        if len(c) == 2:
            right[int(a)] = int(c[1])

    print(f'#{TC+1} ', end="")
    in_order(1)
    print()