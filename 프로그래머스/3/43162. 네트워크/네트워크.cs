using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    bool[] v;
    int N;
    public int solution(int n, int[,] computers) {
        int answer = 0;
        v = new bool[n];
        N = n;
        for (int i=0; i<N; ++i) {
            if (!v[i]) {
                answer++;
                v[i] = true;
                dfs(i, computers);
            }
        }
        
        
        return answer;
    }
    public void dfs(int cur, int[,] graph){
        for (int nxt=0; nxt<N; ++nxt) {
            if (graph[cur,nxt] == 0 || v[nxt]) continue;
            v[nxt] = true;
            dfs(nxt, graph);
        }
    }
}