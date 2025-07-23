#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int find_parent(int x, vector<int>& p) {
    if (p[x] != x) {
        p[x] = find_parent(p[x], p);
    }
    return p[x];
}

void union_set(int a, int b, vector<int>& p) {
    int root_a, root_b;
    root_a = find_parent(a, p);
    root_b = find_parent(b, p);

    if (root_a == root_b) {
        return;
    }
    else {
        p[root_b] = root_a;
        return;
    }
}

struct Edge {
    int weight, u, v;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, P;
    cin >> N >> P;

    vector<int> cost(N + 1, 0);
    int min_c = 1001;
    for (int i = 1; i < N + 1; ++i) {
        cin >> cost[i];
        if (min_c > cost[i]) {
            min_c = cost[i];
        }
    }

    vector<Edge> edges(P);

    int s, e, v, tmp;
    for (int i = 0; i < P; ++i) {
        cin >> s >> e >> v;
        tmp = cost[s] + cost[e] + 2 * v;
        edges[i] = { tmp, s, e };

    }

    sort(edges.begin(), edges.end());
    for (int i = 0; i < P; ++i) {
        Edge my_edge = edges[i];
    }

    vector<int> p(N + 1);
    for (int i = 1; i < N + 1; ++i) {
        p[i] = i;
    }


    int cnt = 0, res = 0;
    for (Edge e : edges) {
        if (find_parent(e.u, p) != find_parent(e.v, p)) {
            cnt += 1;
            res += e.weight;
            union_set(e.u, e.v, p);
        }
        if (cnt == N - 1) {
            break;
        }
    }
    res += min_c;
    cout << res;



    return 0;
}

