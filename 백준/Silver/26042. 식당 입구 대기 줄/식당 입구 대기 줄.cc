#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <deque>
#include <cstdio>



using namespace std;


int main()
{


    ios::sync_with_stdio(0);
    cin.tie(0);

    deque<int> q;
    int N;
    cin >> N;

    int s_num = 1000001, max_cnt = 0;


    int cmd, a;
    while (N--) {
        cin >> cmd;
        if (cmd == 1) {
            cin >> a;
            q.push_back(a);
            if (max_cnt < q.size()) {
                max_cnt = q.size();
                s_num = q.back();
            }
            else if (max_cnt == q.size()) {
                s_num = min(s_num, q.back());
            }
        }
        else {
            q.pop_front();
        }
    }

    cout << max_cnt << ' ' << s_num;



    return 0;
}

