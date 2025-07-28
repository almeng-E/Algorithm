#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M, K;
long long INF = 1LL << 62;

vector<vector<pair<int, int>>> graph(10001);

struct Item {
    long long cost;
    int left, cur;

    bool operator>(const Item& other) const {
        return cost > other.cost;
    }

};

priority_queue<Item, vector<Item>, greater<Item>> pq;
vector<vector<long long>> dist(10001, vector<long long>(21, INF));

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;
    
    int a, b, c;
    for (int i = 0; i < M; ++i) {
        cin >> a >> b >> c;
        graph[a].push_back({ b, c });
        graph[b].push_back({ a, c });
    }

    dist[1][K] = 0;
    pq.push({ 0, K, 1 });
    int left, cur, nxt, w;
    long long cost, nd;
    while (!pq.empty()) {
        Item item = pq.top();
        cost = item.cost;
        left = item.left;
        cur = item.cur;
        pq.pop();

        if (dist[cur][left] < cost) {
            continue;
        }

        for (auto& p : graph[cur]) {
            nxt = p.first;
            w = p.second;

            nd = cost + w;

            if (dist[nxt][left] > nd) {
                dist[nxt][left] = nd;
                pq.push({ nd, left, nxt });
            }
            if (left > 0 and dist[nxt][left - 1] > cost) {
                dist[nxt][left - 1] = cost;
                pq.push({ cost, left - 1, nxt });
            }
        }
    }

    long long res = INF;
    for (int i = 0; i <= K; ++i) {
        res = min(res, dist[N][i]);
    }
    cout << res;

    return 0;
}

