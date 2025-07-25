#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <string>

using namespace std;


int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int TC;
    cin >> TC;
    while (TC--) {
        int N;
        cin >> N;

        unordered_map<string, int> clothes;
        for (int i = 0; i < N; ++i) {
            string a, b;
            cin >> a >> b;
            if (clothes.count(b)) {
                clothes[b] += 1;
            }
            else {
                clothes[b] = 1;
            }
        }
        int res = 1;
        for (auto& pair: clothes) {
            res *= pair.second+1;
        }
        res -= 1;

        cout << res << '\n';

    }


    return 0;
}

