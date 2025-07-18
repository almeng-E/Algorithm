#include <iostream>

using namespace std;

int main()
{
    int X;
    cin >> X;
    int res = 0, mask = 1;
    while (mask <= X) {
        if (mask & X) {
            res += 1;
        }
        mask <<= 1;
    }

    cout << res;

    return 0;
}

