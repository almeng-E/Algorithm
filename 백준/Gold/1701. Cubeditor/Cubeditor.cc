#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

using ll = long long;
using pll = pair<ll, ll>;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string ss;
    cin >> ss;

    int N = ss.size();

    // prefix 전처리
    const int B1 = 31, MOD1 = 1000000007;
    const int B2 = 37, MOD2 = 1000000009;

    vector<ll> H1(N + 1), P1(N + 1, 1);
    vector<ll> H2(N + 1), P2(N + 1, 1);
    for (int i = 0; i < N; ++i) {
        ll v = ss[i] - 'a' + 1;
        H1[i + 1] = (H1[i] * B1 + v) % MOD1;
        P1[i + 1] = (P1[i] * B1) % MOD1;
        H2[i + 1] = (H2[i] * B2 + v) % MOD2;
        P2[i + 1] = (P2[i] * B2) % MOD2;
    }

    set<pll> used;

    // 이진 탐색
    int left = 1, right = N, res = 0, mid;
    while (left <= right)
    {
        bool found = false;
        used.clear();
        mid = (left + right) / 2;
        for (int i = 0; i <= N - mid; ++i) {
            // 이중 해시 계산
            ll h1 = ((H1[i + mid] - H1[i] * P1[mid]) % MOD1 + MOD1) % MOD1;
            ll h2 = ((H2[i + mid] - H2[i] * P2[mid]) % MOD2 + MOD2) % MOD2;
            pll hsh = { h1, h2 };

            if (used.count(hsh)) {
                found = true;
                break;
            }
            used.insert(hsh);
            
        }
        if (found) {
            left = mid + 1;
            res = mid;
        }
        else {
            right = mid - 1;
        }
    }
    cout << res;

    return 0;
}
