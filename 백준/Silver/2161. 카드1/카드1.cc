#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <deque>



using namespace std;


int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    deque<int> q(N);
    for (int i = 1; i <= N; ++i) {
        q[i - 1] = i;
    }

    while (--N) {
        cout << q.front() << ' ';
        q.pop_front();
        int a = q.front();
        q.pop_front();
        q.push_back(a);
    }
    cout << q.front();

    return 0;
}

