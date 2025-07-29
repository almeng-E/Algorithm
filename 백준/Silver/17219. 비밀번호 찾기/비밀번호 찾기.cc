#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include<iostream>
#include <string>
#include <unordered_map>


using namespace std;

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);


    int N, M;
    cin >> N >> M;
    unordered_map<string, string> pw;

    string url, p;
    while (N--) {
        cin >> url >> p;
        pw[url] = p;
    }
    while (M--) {
        cin >> url;
        cout << pw[url] << '\n';
    }



    return 0;
}

