#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <unordered_set>


using namespace std;


int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N;
    unordered_set<int> s;
    int tmp;
    while (N--) {
        cin >> tmp;
        s.insert(tmp);
    }

    cin >> M;
    while (M--) {
        cin >> tmp;
        cout << s.count(tmp) << '\n';
    }


    return 0;
}

