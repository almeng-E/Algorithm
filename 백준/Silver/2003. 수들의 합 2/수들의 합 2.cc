#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;
int main()
{
    int N, M;
    cin >> N >> M;

    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    int res = 0;
    for (int i = 0; i < N; ++i) {
        int tmp = 0;
        for (int j = i; j < N; ++j) {
            tmp += arr[j];
            if (tmp == M) {
                res += 1;
                break;
            }
            else if (tmp > M) {
                break;
            }
        }
    }

    cout << res;

    return 0;
}

