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
    vector<int> bigger(N);
    for (int i = 0; i < N; ++i) {
        cin >> bigger[i];
    }

    vector<int> arr(N, 0);
    int cnt;
    for (int i = 0; i < N; ++i) {
        cnt = bigger[i];
        for (int j = 0; j < N; ++j) {
            if (arr[j] != 0) {
                continue;
            }
            else {
                if (cnt == 0) {
                    arr[j] = i + 1;
                    break;
                }
                else {
                    cnt -= 1;
                }
            }
        }
    }

    for (int n : arr) {
        cout << n << ' ';
    }



    return 0;
}

