def heuri_max(i):
    max_prob = 1
    for x in range(i, N):
        max_prob *= row_max[x] / 100
    return max_prob



def backtrack(depth, tmp):
    global res
    if depth == N-1:
        res = max(res, round(tmp*100, 6))
        return

    # 가지치기
    if tmp * heuri_max(depth+1) * 100 < res:
        return


    for n_work in best_indexes[depth+1]:
        if not visited[n_work]:
            visited[n_work] = True
            backtrack(depth+1, tmp*percent[depth+1][n_work]/100)
            visited[n_work] = False



T = int(input())
for TC in range(T):
    N = int(input())

    percent = [list(map(int, input().split())) for _ in range(N)]

    # 휴리스틱(?)
    best_indexes = [[] for _ in range(N)]
    row_max = []
    for i in range(N):
        tmp_li = []
        for j in range(N):
            tmp_li.append((percent[i][j], j))
        tmp_li.sort(key=lambda x:x[0], reverse=True)
        for j in range(N):
            best_indexes[i].append(tmp_li[j][1])
        row_max.append(tmp_li[0][0])


    res = 0.0
    visited = [False] * N

    for i in range(N):
        visited[i] = True
        backtrack(0, percent[0][i]/100)
        visited[i] = False

    print(f"#{TC + 1} {res:.6f}")