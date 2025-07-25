#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;


int main()
{
    //freopen("input.txt", "r", stdin);

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    
    priority_queue<pair<int, int>> pq; // abs-min-heap!!
    int cmd;
    
    while (N--) {
        cin >> cmd;

        if (cmd) {
            int sec = 1;
            if (cmd < 0) {
                cmd *= -1;
                sec = -1;
            }
            pq.push({ -cmd, -sec });

        }
        else {
            if (pq.empty()) {
                cout << 0 << '\n';
            }
            else {
                auto p = pq.top();
                int a, b;
                a = p.first;
                b = p.second;

                a *= -1;
                b *= -1;

                pq.pop();

                if (b == -1) {
                    cout << -a << '\n';
                }
                else {
                    cout << a << '\n';
                }
            }
            
        }

    }


    return 0;
}

