def dfs(current_node, li):
    li.append(graph[current_node][0])
    if graph[current_node][0] == 1:
        return
    else:
        dfs(graph[current_node][0], li)

def dfs_result(starting_node):
    global res
    visited[starting_node] = True
    res += 1
    for next_node in original[starting_node]:
        if not visited[next_node]:
            dfs_result(next_node)

T = int(input())
for TC in range(T):
    V, E, node1, node2 = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    original = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    node1_parents = []
    node2_parents = []

    # 그래프 초기화
    arr = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        graph[arr[i+1]].append(arr[i])
        original[arr[i]].append(arr[i+1])
    # 경로 저장
    dfs(node1, node1_parents)
    dfs(node2, node2_parents)


    # top_node
    for i in range(min(len(node1_parents), len(node2_parents))):
        if node1_parents[-1-i] == node2_parents[-1-i]:
            top_node = node1_parents[-1-i]
        else:
            break
    res = 0
    dfs_result(top_node)
    print(f'#{TC+1} {top_node} {res}')