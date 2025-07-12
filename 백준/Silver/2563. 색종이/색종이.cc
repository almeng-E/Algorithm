#include <iostream>
#include <vector>

using namespace std;



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<vector<int>> board(100, vector<int>(100, 0));

    int n;
    cin >> n;

    int x, y;
    while (n--) {
        cin >> x >> y;

        for (int i = x; i < x+10; ++i) {
            for (int j = y; j < y+10; ++j) {
                board[i][j] = 1;
            }
        }

    }

    int res;
    res = 0;
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j < 100; ++j) {
            res += board[i][j];
        }
    }

    cout << res;

    return 0;
}

