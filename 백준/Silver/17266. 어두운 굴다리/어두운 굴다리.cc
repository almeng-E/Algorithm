#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> dist;
    int bef = 0;
    int cur;
    while (M--) {
        cin >> cur;
        dist.push_back(cur - bef);
        bef = cur;
    }
    dist.push_back(N - bef);

    int left = 1;
    int right = 100000;
    int res = 0;
    int mid;
    bool ok;
    while (left <= right) {
        ok = true;
        mid = (left + right) / 2;
        for (int i = 0; i < dist.size(); ++i) {
            if (i == 0 or i == (dist.size() - 1)) {
                if (dist[i] > mid) {
                    ok = false;
                    break;
                }
            }
            else {
                if (dist[i] > 2 * mid) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) {
            right = mid - 1;
            res = mid;
        }
        else {
            left = mid + 1;
        }
    }

    cout << res;



    return 0;
}

