#include <iostream>
#include <vector>
#include <queue>

using namespace std;

using pii = pair<int, int>;


int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);

    const int INF = 1e9;
    int N, M;
    cin >> N >> M;

    vector<vector<pii>> graph(N + 1);

    int a, b, c;
    while (M--) {
        cin >> a >> b >> c;

        graph[a].push_back(make_pair(b, c));
        graph[b].push_back(make_pair(a, c));
    }

    priority_queue<pii, vector<pii>, greater<pii>> pq;
    vector<int> dist(N + 1, INF);

    dist[1] = 0;
    pq.push(make_pair(0, 1));

    int cur, d, nxt, w, nd;
    pii p;
    while (!pq.empty()) {
        p = pq.top();
        d = p.first;
        cur = p.second;
        pq.pop();

        if (dist[cur] < d) {
            continue;
        }

        for (pii np : graph[cur]) {
            nxt = np.first;
            w = np.second;

            nd = d + w;
            if (dist[nxt] > nd) {
                dist[nxt] = nd;
                pq.push(make_pair(nd, nxt));
            }
        }
    }

    cout << dist[N];




    return 0;
}

