#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <string>
#include <set>
#include <unordered_map>

using namespace std;


struct Question {
    int grade, id;

    bool operator<(const Question& o) const {
        if (grade != o.grade) {
            return grade < o.grade;
        }
        return id < o.id;
    }

};

set<Question> S;
unordered_map<int, int> cur;

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, P, L;
    cin >> N;
    while (N--) {
        cin >> P >> L;
        S.insert({ L, P });
        cur[P] = L;
    }
    int M;
    cin >> M;
    string cmd;
    int X;
    while (M--) {
        cin >> cmd;
        if (cmd[0] == 'a') {
            cin >> P >> L;
            S.insert({ L, P });
            cur[P] = L;

        }
        else if (cmd[0] == 'r') {
            cin >> X;
            if (X == 1) {
                auto it = S.rbegin();
                cout << it->id << '\n';

            }
            else {
                auto it = S.begin();
                cout << it->id << '\n';
            }

        }
        else {
            cin >> P;
            L = cur[P];
            cur.erase(P);
            S.erase({ L, P });
        }

    }


    return 0;
}

