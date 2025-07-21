#include <iostream>
#include <string>

using namespace std;

int update(int &my, int &mm, int &md, int ny, int nm, int nd, string &mn, string nn) {
    my = ny;
    mm = nm;
    md = nd;
    mn = nn;

    return 0;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int minD = 32, minM = 13, minY = 2020, maxD = 0, maxM = 0, maxY = 1988;
    int N;
    cin >> N;

    string minName, maxName;

    while (N--) {
        string name;
        int d, m, y;
        cin >> name >> d >> m >> y;

        // 적은 사람 비교
        if (minY > y) {
            update(minY, minM, minD,
                y, m, d,
                minName, name);
        }
        else if (minY == y) {
            if (minM > m) {
                update(minY, minM, minD,
                    y, m, d,
                    minName, name);
            }
            else if (minM == m and minD > d) {
                update(minY, minM, minD,
                    y, m, d,
                    minName, name);
            }
        }

        if (maxY < y) {
            update(maxY, maxM, maxD,
                y, m, d,
                maxName, name);
        }
        else if (maxY == y) {
            if (maxM < m) {
                update(maxY, maxM, maxD,
                    y, m, d,
                    maxName, name);
            }
            else if (maxM == m and maxD < d) {
                update(maxY, maxM, maxD,
                    y, m, d,
                    maxName, name);
            }
        }
    }

    cout << maxName << '\n' << minName;

    return 0;
}

