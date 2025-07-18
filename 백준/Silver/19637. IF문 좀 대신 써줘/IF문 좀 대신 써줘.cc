#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>


using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<string> names(N);
    vector<int> power(N);

    string ss;
    int ii;
    for (int i = 0; i < N; ++i) {
        cin >> ss >> ii;
        names[i] = ss;
        power[i] = ii;
    }

    int v, idx;
    while (M--) {
        cin >> v;
        idx = lower_bound(power.begin(), power.end(), v) - power.begin();
        cout << names[idx] << '\n';
    }

    return 0;
}

