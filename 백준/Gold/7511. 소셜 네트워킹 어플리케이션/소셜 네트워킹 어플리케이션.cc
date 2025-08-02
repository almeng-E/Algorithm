#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <unordered_map>

using namespace std;


unordered_map<int, int>p;


int find_p(int x) {
    if (p[x] != x) {
        p[x] = find_p(p[x]);
    }
    return p[x];
}

void union_set(int a, int b) {
    int rt_a, rt_b;
    rt_a = find_p(a);
    rt_b = find_p(b);

    if (rt_a == rt_b) {
        return;
    }
    else {
        p[rt_b] = rt_a;
    }
}



int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc) {
        p.clear();
        cout << "Scenario " << tc << ":\n";
        int N, K;
        cin >> N >> K;

        int a, b;
        while (K--) {
            cin >> a >> b;
            if (!p.count(a)) {
                p[a] = a;
            }
            if (!p.count(b)) {
                p[b] = b;
            }
            if (find_p(a) != find_p(b)) {
                union_set(a, b);
            }
        }
        int M, u, v;
        cin >> M;
        while (M--) {
            cin >> u >> v;
            if (!p.count(u)) {
                p[u] = u;
            }
            if (!p.count(v)) {
                p[v] = v;
            }
            if (find_p(u) == find_p(v)) {
                cout << 1 << '\n';
            }
            else {
                cout << 0 << '\n';
            }
        }
        cout << '\n';


    }

    return 0;
}

