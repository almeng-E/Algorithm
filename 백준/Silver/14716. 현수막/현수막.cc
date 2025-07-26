#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <vector>


using namespace std;

void dfs(int x, int y, int cnt, int N, int M, vector<vector<int>>& board, vector<int>& dx, vector<int>& dy) {
    board[x][y] = cnt;

    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 or nx >= N or ny < 0 or ny >= M) {
            continue;
        }

        if (board[nx][ny] != -1) {
            continue;
        }

        dfs(nx, ny, cnt, N, M, board, dx, dy);

    }


}

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M, 0));

    vector<pair<int, int>> coords;

    int x;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> x;
            if (x) {
                coords.push_back({ i, j });
                board[i][j] = -1;
            }

        }
    }

    int cnt = 0;

    vector<int> dx = {0, 0, 1, -1, 1, 1, -1, -1};
    vector<int> dy = { 1, -1, 0, 0, 1, -1, 1, -1 };

    
    for (auto& p : coords) {
        int x = p.first;
        int y = p.second;


        if (board[x][y] != -1) {
            continue;
        }

        cnt += 1;
        dfs(x, y, cnt, N, M, board, dx, dy);


    }

    cout << cnt;

    return 0;
}

