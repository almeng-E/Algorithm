#include <iostream>
#include <string>

using namespace std;


int main()
{
    string ISBN;
    cin >> ISBN;

    int s = 0, a;
    bool weight;
    for (int i = 0; i < 13; ++i) {
        if (ISBN[i] == '*') {
            if (i & 1) {
                weight = true;
            }
            else {
                weight = false;
            }
            continue;
        }
        a = ISBN[i] - '0';
        if (i & 1) {
            s += (3 * a);
        }
        else {
            s += a;
        }

    }

    int ans;
    for (int i = 0; i < 10; ++i) {
        if (weight) {
            ans = s + 3 * i;
        }
        else {
            ans = s + i;
        }
        if (ans % 10 == 0) {
            cout << i;
            return 0;
        }
    }



    return 0;
}

