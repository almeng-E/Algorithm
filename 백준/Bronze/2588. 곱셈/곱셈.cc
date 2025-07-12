#include <iostream>
#include <string>
#include <cmath>

using namespace std;



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int one, digit, res;
    string two;

    cin >> one >> two;
    res = 0;
    for (int i = 0; i < 3; ++i) {
        digit = (two[2 - i] - '0');
        cout << one * digit << '\n';
        res += one * digit * pow(10, i);
    }
    cout << res;


    return 0;
}

