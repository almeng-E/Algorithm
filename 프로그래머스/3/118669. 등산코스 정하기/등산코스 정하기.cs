using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int n, int[,] paths, int[] gates, int[] summits) {
        int INF = int.MaxValue/2;
        int[] ans = new int[2]{INF, INF};
        
        // isSummit
        bool[] isSummit = new bool[n+1];
        foreach (int v in summits) {
            isSummit[v] = true;
        }
        Array.Sort(summits);
        
        // 그래프 초기화
        var G = new List<(int nxt, int w)>[n+1];        
        for (int i=0; i<=n; ++i) {
            G[i] = new List<(int nxt, int w)>();
        }
        for (int i=0; i<paths.GetLength(0); ++i) {
            int a = paths[i,0], b = paths[i,1], c = paths[i,2];
            G[a].Add((b, c));
            G[b].Add((a, c));
        }
        
        // 다익스트라
        var dist = new int[n+1];
        for (int i=0; i<=n; ++i) {
            dist[i] = INF;
        }

        var PQ = new SortedSet<(int d, int cur)>();
        foreach (int st in gates) {
            dist[st] = 0;
            PQ.Add((0, st));
        }

        while (PQ.Count > 0) {
            var top = PQ.Min;
            PQ.Remove(top);
            int d = top.d;
            int cur = top.cur;

            if (dist[cur] < d) continue;

            foreach (var edge in G[cur]) {
                int nxt = edge.nxt, w = edge.w;
                int nd = Math.Max(d, w);
                if (dist[nxt] > nd) {
                    dist[nxt] = nd;
                    if (isSummit[nxt]) continue;
                    PQ.Add((nd, nxt));
                }
            }
        }
        foreach (int v in summits) {
            if (ans[1] > dist[v]) {
                ans[0] = v;
                ans[1] = dist[v];
            }
        }

        
        
        return ans;
    }
}