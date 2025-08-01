#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;



int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> cnt(N + 1, 0);
    vector<tuple<int, int, int>> sc;
    int a, b, c;
    while (N--) {
        cin >> a >> b >> c;
        sc.push_back({ c, a, b });
    }
    sort(sc.begin(), sc.end(), greater<tuple<int, int, int>>());

    int got = 0;
    for (int i = 0; i < sc.size(); ++i) {
        auto& t = sc[i];
        if (got == 3) {
            break;
        }
        if (cnt[get<1>(t)] < 2) {
            cout << get<1>(t) << ' ' << get<2>(t) << '\n';
            cnt[get<1>(t)] += 1;
            got += 1;
        }

    }

    return 0;
}

