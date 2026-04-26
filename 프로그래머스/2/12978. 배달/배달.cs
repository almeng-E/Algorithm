using System;
using System.Collections.Generic;
using System.Linq;

class Solution {
    public int solution(int N, int[,] road, int K)     {
        var G = new List<(int nxt, int w)>[N+1];
        for (int i=0; i<=N; ++i) {
            G[i] = new List<(int nxt, int w)>();
        }
        for (int i=0; i<road.GetLength(0); ++i) {
            int a=road[i,0], b=road[i,1], c=road[i,2];
            G[a].Add((b, c));
            G[b].Add((a, c));
        }
        int INF = (int)1e9;
        var dist = new int[N+1];
        for (int i=0; i<=N; ++i) {
            dist[i] = INF;
        }
        dist[1] = 0;
        var PQ = new SortedSet<(int d, int cur)>();
        PQ.Add((0, 1));
        
        while (PQ.Count > 0) {
            var top = PQ.Min;
            int d = top.d, cur=top.cur;
            PQ.Remove(top);
            
            if (dist[cur] < d) continue;
            
            foreach (var item in G[cur]) {
                int nxt=item.nxt, w=item.w;
                int nd = d+w;
                if (dist[nxt] > nd) {
                    dist[nxt] = nd;
                    PQ.Add((nd, nxt));
                }
            }
        }
        
        int answer = 0;
        for (int i=1; i<=N; ++i) {
            if (dist[i] <= K) answer++;
        }
        return answer;
    }
}