#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <deque>
#include <vector>

using namespace std;


int main()
{
    //freopen("input.txt", "r", stdin);

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    deque<int> q;
    vector<int> cmd(N);
    for (int i = N - 1; i >= 0; --i) {
        cin >> cmd[i];
    }

    for (int i = 1; i <= N; ++i) {
        
        if (cmd[i-1] == 1) {
            q.push_front(i);
        }
        else if (cmd[i-1] == 2) {
            int top;
            top = q.front();
            q.pop_front();
            q.push_front(i);
            q.push_front(top);

        }
        else {
            q.push_back(i);

        }
    }

    for (int i = 0; i < N; ++i) {
        cout << q[i] << ' ';
    }



    return 0;
}

