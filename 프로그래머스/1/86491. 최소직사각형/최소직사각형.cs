using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[,] sizes) {
        var rec = new List<(int l, int s)>();
        int N = sizes.GetLength(0);
        for (int i=0; i<N; ++i) {
            int a = sizes[i, 0];
            int b = sizes[i, 1];
            rec.Add((Math.Max(a, b), Math.Min(a, b)));
        }

        int LONG = 0;
        int SHORT = 0;
        foreach (var e in rec) {
            LONG = Math.Max(LONG, e.l);
            SHORT = Math.Max(SHORT, e.s);
        }
        
        int answer = LONG*SHORT;        
        return answer;
    }
}