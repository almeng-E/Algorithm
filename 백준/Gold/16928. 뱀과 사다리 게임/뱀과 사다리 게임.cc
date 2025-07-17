#include <iostream>
#include <vector>
#include <queue>



using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;
    
    const int INF = 1e9;
    vector<int> graph(101, 0);
    int x, y;
    while (N--) {
        cin >> x >> y;
        graph[x] = y;
    }
    
    while (M--)
    {
        cin >> x >> y;
        graph[x] = y;
    }

    queue<pair<int, int>> q;
    vector<int> dist(101, -1);
    q.push({1, 0});
    dist[1] = 0;

    pair<int, int> p;
    int cur, d;
    while (!q.empty()) {
        p = q.front();
        cur = p.first;
        d = p.second;
        q.pop();


        if (cur == 100) {
            cout << d;
            return 0;
        }

        for (int r = 1; r <= 6; ++r) {
            int nxt = cur + r;

            if (nxt > 100) {
                continue;
            }

            if (graph[nxt] != 0) {
                nxt = graph[nxt];
            }

            if (dist[nxt] == -1) {
                dist[nxt] = d + 1;
                q.push({ nxt, d + 1 });
            }

        }

        
    }

    cout << dist[100];
    return 0;
}

