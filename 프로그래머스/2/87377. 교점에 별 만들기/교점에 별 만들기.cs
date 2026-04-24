using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(int[,] line) {
        int N = line.GetLength(0);
        long a, b, c, d, e, f;
        var pos = new HashSet<(long x, long y)>();
        long minX=long.MaxValue, minY=long.MaxValue, maxX=long.MinValue, maxY=long.MinValue;
        for (int i=0; i<N-1; ++i) {
            a = line[i,0];
            b = line[i,1];
            e = line[i,2];
            for (int j=i+1; j<N; ++j) {
                c = line[j,0];
                d = line[j,1];
                f = line[j,2];
                
                if ((a*d - b*c) == 0) continue;
                if (((b*f-e*d)%(a*d-b*c)) != 0 || ((e*c-a*f)%(a*d-b*c)) != 0) continue;
                long x = (b*f-e*d)/(a*d-b*c);
                long y = (e*c-a*f)/(a*d-b*c);
                pos.Add((x, y));
                minX = Math.Min(minX, x);
                minY = Math.Min(minY, y);
                maxX = Math.Max(maxX, x);
                maxY = Math.Max(maxY, y);
            }
        }
        int W = (int)(maxX-minX+1);
        int H = (int)(maxY-minY+1);
        
        var ret = new char[H][];
        for (int i=0; i<H; ++i) {
            ret[i] = new char[W];
            for (int j=0; j<W; ++j) {
                ret[i][j] = '.';
            }
        }
        foreach (var p in pos) {
            int x = (int)(p.x-minX);
            int y = (int)(maxY-p.y);
            ret[y][x] = '*';
        }
        
        string[] answer = new string[H];
        for (int i=0; i<H; ++i) {
            answer[i] = new string(ret[i]);
        }
        
        return answer;
    }
}