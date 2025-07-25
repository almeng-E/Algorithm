#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;


int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    int cmd;
    priority_queue<int> pq;
    while (N--) {
        cin >> cmd;
        if (cmd == 0) {
            int tmp;
            if (pq.empty()) {
                cout << 0 << '\n';
            }
            else {
                tmp = pq.top();
                pq.pop();
                cout << tmp << '\n';
            }
        }
        else {
            pq.push(cmd);
        }


    }



    return 0;
}

