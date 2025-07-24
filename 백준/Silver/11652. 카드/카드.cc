#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <unordered_map>


using namespace std;


int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);


    int N;
    cin >> N;

    unordered_map<long long, int> cnt;

    long long num;
    int MAX=0;
    long long res;
    while (N--) {
        cin >> num;
        if (cnt.count(num)) {
            cnt[num] += 1;
        }
        else {
            cnt[num] = 1;
        }
        if (MAX < cnt[num]) {
            MAX = cnt[num];
            res = num;
        }
        else if (MAX == cnt[num]) {
            res = min(res, num);
        }
    }

    cout << res;

    return 0;
}

