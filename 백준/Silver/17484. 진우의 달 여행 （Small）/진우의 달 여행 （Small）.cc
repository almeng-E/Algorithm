#include <iostream>
#include <vector>
#include <queue>



using namespace std;

int main()
{
    int ddd[] = { -1, 0, 1 };

    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M, 0));

    int tmp;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> tmp;
            board[i][j] = tmp;

        }
    }
    int INF = 1e5;
    // [x][y][di]
    vector<vector<vector<int>>> dist(N, vector<vector<int>>(M, vector<int>(3, INF)));

    for (int i = 0; i < M; ++i) {
        dist[0][i][0] = board[0][i];
        dist[0][i][1] = board[0][i];
        dist[0][i][2] = board[0][i];
    }

    int ny, nc;
    for (int i = 0; i < N-1; ++i) {
        for (int j = 0; j < M; ++j) {
            for (int prev : ddd) {
                for (int nxt : ddd) {
                    if (prev == nxt) {
                        continue;
                    }

                    ny = j + nxt;

                    if (ny >= 0 and ny < M) {
                        nc = dist[i][j][prev+1] + board[i + 1][ny];
                        dist[i + 1][ny][nxt+1] = min(dist[i + 1][ny][nxt+1], nc);
                    }
                }
            }
        }
    }

    int res = INF;
    for (int j = 0; j < M; ++j) {
        for (int di = 0; di < 3; ++di) {
            res = min(res, dist[N - 1][j][di]);
        }
    }
    cout << res;


    return 0;
}

