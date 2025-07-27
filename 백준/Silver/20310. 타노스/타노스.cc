#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <queue>
#include <string>
#include <vector>


using namespace std;



int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    string S;
    cin >> S;
    
    int LEN = S.length();

    vector<int>zero;
    vector<int>one;

    for (int i = 0; i < LEN; ++i) {
        if (S[i] == '1') {
            one.push_back(i);
        }
        else {
            zero.push_back(i);
        }
    }

    priority_queue<int, vector<int>, greater<int>> lazy;
    int zs = zero.size();
    int oos = one.size() / 2;
    for (int i = 0; i < oos; ++i) {
        lazy.push(one[i]);
    }
    for (int i = zs - 1; i >= zs/2; --i) {
        lazy.push(zero[i]);
    }
    
    string res;
    for (int i = 0; i < LEN; ++i) {
        if (!lazy.empty() and i == lazy.top()) {
            lazy.pop();
            continue;
        }
        res += S[i];

    }
    
    
    cout << res;


    return 0;
}

