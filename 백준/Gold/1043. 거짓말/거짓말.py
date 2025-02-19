import sys
sys.setrecursionlimit(10**6)



'''
노드 만들기
cops 저장
파티 정보 쭉 저장
그래프 정보 저장
순회하며 정답 체크
'''

def dfs(v):
    know_truth[v] = True

    for next_node in graph[v]:
        if not know_truth[next_node]:
            dfs(next_node)

# N: 사람 수, M: 파티 수
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
know_truth = [False] * (N+1)

_, *starting_nodes = map(int, input().split())

# 파티 정보 저장
parties = []
for _ in range(M):
    no, *party = map(int, input().split())
    parties.append(party)

# 그래프 정보 저장
for party in parties:
    for i in range(len(party)):
        for j in range(i, len(party)):
            graph[party[i]].append(party[j])
            graph[party[j]].append(party[i])

for s_node in starting_nodes:
    dfs(s_node)

res = 0
for party in parties:
    for ppl in party:
        if know_truth[ppl]:
            break
    else:
        res += 1
print(res)
