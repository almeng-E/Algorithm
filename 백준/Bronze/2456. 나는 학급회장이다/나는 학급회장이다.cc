#include <iostream>
#include <vector>


using namespace std;


int main()
{
    cin.tie(0);
    ios::sync_with_stdio(0);

    int N;
    cin >> N;

    vector<vector<int>> cnt(4, vector<int>(4, 0));

    int a;
    while (N--) {
        for (int i = 1; i < 4; ++i) {
            cin >> a;
            cnt[i][a] += 1;
            cnt[i][0] += a;
        }
    }

    // 0 비교
    int z = 0;
    vector<int> cand;
    for (int i = 1; i < 4; ++i) {
        if (z < cnt[i][0]) {
            z = cnt[i][0];
            cand.clear();
            cand.push_back(i);
        }
        else if (z == cnt[i][0]) {
            cand.push_back(i);
        }
    }
    if (cand.size() == 1) {
        cout << cand[0] << ' ' << z;
        return 0;
    }
    int th = 0;
    vector<int> three;
    for (int c : cand) {
        if (th < cnt[c][3]) {
            th = cnt[c][3];
            three.clear();
            three.push_back(c);
        }
        else if (th == cnt[c][3]) {
            three.push_back(c);
        }
    }
    if (three.size() == 1) {
        cout << three[0] << ' ' << z;
        return 0;
    }

    int tw = 0;
    vector<int> two;
    for (int t : three) {
        if (tw < cnt[t][2]) {
            tw = cnt[t][2];
            two.clear();
            two.push_back(t);
        }
        else if (tw == cnt[t][2]) {
            two.push_back(t);
        }
    }
    if (two.size() == 1) {
        cout << two[0] << ' ' << z;
    }
    else {
        cout << 0 << ' ' << z;
    }


    return 0;
}

