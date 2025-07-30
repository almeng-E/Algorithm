#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <string>
#include <set>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct Q {
    int grade, num;

    bool operator<(const Q& o) const {
        if (grade != o.grade) {
            return grade < o.grade;
        }
        return num < o.num;
    }

    bool operator>(const Q& o) const {
        if (grade != o.grade) {
            return grade > o.grade;
        }
        return num > o.num;
    }
};
unordered_map<int, set<Q>> POOL;

struct Info {
    int grade, algo;
};
unordered_map<int, Info> LIST;

int add(int P, int L, int G) {
    LIST[P] = { L, G };
    POOL[G].insert({ L, P });
    return 0;
}

int solved(int P) {
    int L, G;
    Info p = LIST[P];
    L = p.grade;
    G = p.algo;
    LIST.erase(P);
    POOL[G].erase({ L, P });
    return 0;
}

int r1(int G, int x) {
    if (x == 1) {
        auto p = POOL[G].rbegin();
        return p->num;
    }
    else {
        auto p = POOL[G].begin();
        return p->num;
    }
}

int r2(int x) {
    int res_g, res_num;
    if (x == 1) {
        res_g = 0;
        res_num = 0;
        for (auto it = POOL.begin(); it != POOL.end(); ++it) {
            int g, num;
            if (it->second.empty()) {
                continue;
            }
            auto p = it->second.rbegin();
            g = p->grade;
            num = p->num;

            if (res_g < g) {
                res_g = g;
                res_num = num;
            }
            else if (res_g == g){
                res_num = max(res_num, num);
            }
        }
    }
    else {
        res_g = 1000;
        res_num = 100000;
        for (auto it = POOL.begin(); it != POOL.end(); ++it) {
            int g, num;
            if (it->second.empty()) {
                continue;
            }
            auto p = it->second.begin();
            g = p->grade;
            num = p->num;

            if (res_g > g) {
                res_g = g;
                res_num = num;
            }
            else if (res_g == g) {
                res_num = min(res_num, num);
            }
        }
    }

    return res_num;
}

int r3(int x, int L) {
    int res_g, res_num;
    if (x == 1) {
        res_g = 100000;
        res_num = 1000000;
        for (auto it = POOL.begin(); it != POOL.end(); ++it) {
            int g, num;
            if (it->second.empty()) {
                continue;
            }
            auto p = it->second.lower_bound({L, 0});
            if (p == it->second.end()) {
                continue;
            }
            g = p->grade;
            num = p->num;

            if (res_g > g) {
                res_g = g;
                res_num = num;
            }
            else if (res_g == g) {
                res_num = min(res_num, num);
            }
        }
        if (res_num == 1000000) {
            return -1;
        }
        else {
            return res_num;
        }
    }
    else {
        res_g = 0;
        res_num = 0;
        for (auto it = POOL.begin(); it != POOL.end(); ++it) {
            int g, num;
            if (it->second.empty()) {
                continue;
            }
            auto p = it->second.lower_bound({ L, 0 });
            if (p == it->second.begin()) {
                continue;
            }
            --p;
            g = p->grade;
            num = p->num;

            if (res_g < g) {
                res_g = g;
                res_num = num;
            }
            else if (res_g == g) {
                res_num = max(res_num, num);
            }
        }
        if (res_num == 0) {
            return -1;
        }
        else {
            return res_num;
        }
    }

    return 0;
}


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, P, L, G, x;
    cin >> N;
    while (N--) {

        cin >> P >> L >> G;
        add(P, L, G);
    }

    int M;
    cin >> M;
    string cmd;

    while (M--) {
        cin >> cmd;

        if (cmd == "recommend") {
            cin >> G >> x;
            int ret = r1(G, x);
            cout << ret << '\n';
        }
        else if (cmd == "recommend2") {
            cin >> x;
            int ret = r2(x);
            cout << ret << '\n';
        }
        else if (cmd == "recommend3") {
            cin >> x >> L;
            int ret = r3(x, L);
            cout << ret << '\n';
        }
        else if (cmd == "add") {
            cin >> P >> L >> G;
            add(P, L, G);
        }
        else {
            cin >> P;
            solved(P);
        }

    }

    return 0;
}

