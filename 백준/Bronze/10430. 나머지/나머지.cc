#include <iostream>
#include <string>

using namespace std;



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int A, B, C;
    cin >> A >> B >> C;
    cout << (A + B) % C << '\n' << ((A % C) + (B % C)) % C << '\n' << (A*B)%C << '\n' << ((A%C) * (B%C)) % C;


    return 0;
}
