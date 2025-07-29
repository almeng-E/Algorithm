#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include<iostream>
#include <string>
#include <set>

using namespace std;

struct Word {
    string ss;
    int len;

    bool operator<(const Word& o) const {
        if (len != o.len){
            return len < o.len;
        }
        return ss < o.ss;
    }
};
set<Word> S;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    string str;
    for (int i = 0; i < N; ++i) {
        cin >> str;
        S.insert({str, (int)str.size()});
    }

    for (auto& w : S) {
        cout << w.ss << '\n';
    }
    





    return 0;
}

