#include <iostream>
#include <string>
#include <vector>

using namespace std;



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    vector<int> DP(N, 1);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[i] < arr[j]) {
                DP[i] = max(DP[i], DP[j] + 1);
            }
        }
    }

    int best = 0;
    for (int cnt : DP) {
        best = max(best, cnt);
    }

    cout << N - best;
    return 0;
}

