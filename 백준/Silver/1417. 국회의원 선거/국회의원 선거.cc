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

    int N, d;
    cin >> N >> d;

    priority_queue<int> pk;
    int tmp;
    for (int i = 0; i < N - 1; ++i) {
        cin >> tmp;
        pk.push(tmp);
    }
    
    int res = 0;
    while (!pk.empty() and d <= pk.top()) {
        tmp = pk.top();
        pk.pop();
        tmp -= 1;
        res += 1;
        d += 1;
        pk.push(tmp);

    }
    cout << res;


    return 0;
}

