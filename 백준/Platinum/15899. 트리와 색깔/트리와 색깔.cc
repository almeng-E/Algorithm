#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct State {
    int x, y, z;
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int MOD = 1000000007;

    int N, M, C;
    cin >> N >> M >> C;

    vector<int> colors = { 0 };
    int c;
    for (int i = 0; i < N; ++i) {
        cin >> c;
        colors.push_back(c);
    }

    vector<vector<int>> graph(N + 1);

    int a, b;
    for (int i = 0; i < N - 1; ++i) {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    // DFS 오일러 경로
    vector<int> in_o(N + 1, 0);
    vector<int> out_o(N + 1, 0);
    int cnt = 0;
    vector<State> stack;

    stack.push_back({ 1, 0, 1 });     // cur, bef, stat(1진입 0탈출)

    int cur, bef, stat;
    State te;
    while (!stack.empty()) {
        te = stack.back();
        stack.pop_back();
        cur = te.x;
        bef = te.y;
        stat = te.z;

        if (stat == 1) {
            cnt += 1;
            in_o[cur] = cnt;
            stack.push_back({ cur, bef, 0 });
            for (int nxt : graph[cur]) {
                if (nxt == bef) {
                    continue;
                }
                stack.push_back({ nxt, cur, 1 });
            }
        }
        else {
            out_o[cur] = cnt;
        }
    }

    // merge-sort-tree 생성
    int LEN = 1;
    while (LEN < N) {
        LEN <<= 1;
    }
    int SIZE = LEN << 1;

    vector<vector<int>> tree(SIZE);

    for (int i = 1; i < N + 1; ++i) {
        tree[in_o[i] - 1 + LEN].push_back(colors[i]);
    }

    for (int i = LEN - 1; i > 0; --i) {
        tree[i].resize(tree[i * 2].size() + tree[i*2 + 1].size());

        merge(tree[i * 2].begin(), tree[i * 2].end(),
            tree[i * 2 + 1].begin(), tree[i * 2 + 1].end(),
            tree[i].begin());
    }

    int res = 0;
    int vi, ci, left, right, idx;
    while (M--) {
        cin >> vi >> ci;

        left = in_o[vi] - 1 + LEN;
        right = out_o[vi] - 1 + LEN;

        while (left <= right) {
            if (left & 1) {
                idx = upper_bound(tree[left].begin(), tree[left].end(), ci) - tree[left].begin();
                res += idx;
                res %= MOD;
                left += 1;
            }
            if (!(right & 1)) {
                idx = upper_bound(tree[right].begin(), tree[right].end(), ci) - tree[right].begin();
                res += idx;
                res %= MOD;
                right -= 1;
            }

            left >>= 1;
            right >>= 1;
        }
        res %= MOD;
    }
    cout << res;
    return 0;
}

