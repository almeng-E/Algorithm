#include <iostream>
#include <vector>
#include <unordered_set>


using namespace std;

int main() 
{

    int N, M;
    cin >> N >> M;
    vector<int> train(N + 1, 0);
   
    int cmd, i, x, mask, overflow = 1 << 21;
    while (M--) {
        cin >> cmd;
        if (cmd == 1) {
            cin >> i >> x;
            mask = (1 << x);
            train[i] |= mask;

        } 
        else if (cmd == 2) {
            cin >> i >> x;
            mask = (1 << x);
            train[i] &= ~mask;

        }
        else if (cmd == 3) {
            cin >> i;
            train[i] <<= 1;
            train[i] &= (overflow - 1);


        }
        else {
            cin >> i;
            train[i] >>= 1;
            train[i] &= ~1;
        }
    }

    unordered_set<int> used;
    int st, res = 0;
    for (int i = 1; i < N + 1; ++i) {
        st = train[i];
        if (used.count(st)) {
            continue;
        }
        used.insert(st);
        res += 1;
    }
    cout << res;

    return 0;
}

