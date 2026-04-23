using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[,] jobs) {
        int answer = 0;
        var RQ = new SortedSet<(int durTime, int sTime, int id)>();
        var J = new List<(int sTime, int durTime, int id)>();
        int LEN = jobs.GetLength(0);
        
        for (int i=0; i<LEN; ++i) {
            int s = jobs[i, 0];
            int l = jobs[i, 1];
            J.Add((s, l, i));
        }
        J.Sort();
        
        int curTime = 0;
        int jIdx = 0;
        int cnt = 0;
        while (cnt < LEN) {
            while ((jIdx < LEN) && (J[jIdx].sTime <= curTime)) {
                RQ.Add((J[jIdx].durTime, J[jIdx].sTime, J[jIdx].id));
                jIdx++;
            }
            
            if (RQ.Count == 0) {
                curTime = J[jIdx].sTime;
                continue;
            }
            
            var nxt = RQ.Min;
            RQ.Remove(nxt);
            cnt++;
            curTime += nxt.durTime;
            answer += curTime-nxt.sTime;            
        }
        
        answer /= LEN;
        return answer;
    }
}