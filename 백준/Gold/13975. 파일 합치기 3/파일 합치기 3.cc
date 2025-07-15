#include <iostream>
#include <vector>
#include <queue>


using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T, K;
    
    cin >> T;
    priority_queue<long long, vector<long long>, greater<long long>> pq;
    long long tmp, res, a, b;
    while (T--) {
        cin >> K;
        while (K--) {
            cin >> tmp;
            pq.push(tmp);
        }
        res = 0;
        while (pq.size() > 1) {
            a = pq.top();
            pq.pop();
            b = pq.top();
            pq.pop();
            pq.push(a + b);
            res += (a + b);
        }
        pq.pop();

        cout << res << '\n';
    }

    return 0;
}

