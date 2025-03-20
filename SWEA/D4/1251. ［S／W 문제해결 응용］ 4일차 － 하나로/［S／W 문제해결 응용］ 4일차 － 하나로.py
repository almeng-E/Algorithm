from itertools import combinations

def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]

def union_set(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)
    if root_a == root_b:
        return
    else:
        p[root_b] = root_a


T = int(input())
for TC in range(T):

    N = int(input())

    x_pos = list(map(int, input().split()))
    y_pos = list(map(int, input().split()))

    nCr = combinations(range(N), 2)

    edges = []
    for comb in nCr:
        a, b = comb
        edges.append((a, b, (x_pos[a] - x_pos[b]) ** 2 + (y_pos[a] - y_pos[b]) ** 2))

    edges.sort(key=lambda x: x[2])

    p = [i for i in range(N + 1)]

    e_cnt = 0
    res = 0.0
    E = float(input())
    for a, b, c in edges:
        if find_parent(a) == find_parent(b):
            continue
        else:
            union_set(a, b)
            res += c*E
            e_cnt += 1

        if e_cnt == (N - 1):
            break
    print(f'#{TC+1} {round(res)}')