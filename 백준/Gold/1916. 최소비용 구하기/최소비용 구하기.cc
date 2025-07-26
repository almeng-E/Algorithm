#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>


using namespace std;


int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<vector<pair<int, int>>> graph(N + 1);
    for (int i = 0; i < M; ++i) {
        int u, v, d;
        cin >> u >> v >> d;
        graph[u].push_back({ v, d });

    }

    int s, e;
    cin >> s >> e;
    const int INF = 1e9;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    vector<int> distance(N + 1, INF);
    
    distance[s] = 0;
    pq.push({ 0, s });

    int d, cur;
    while (!pq.empty()) {
        auto& p = pq.top();
        d = p.first;
        cur = p.second;
        pq.pop();

        if (distance[cur] < d) {
            continue;
        }

        int nxt, w, nd;
        for (auto& pp : graph[cur]) {
            nxt = pp.first;
            w = pp.second;

            nd = d + w;
            if (distance[nxt] > nd) {
                distance[nxt] = nd;
                pq.push({ nd, nxt });
            }
        }
    }

    cout << distance[e];
  
    return 0;
}

