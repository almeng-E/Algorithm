using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int N = progresses.Length;
        var li = new List<int>();
        for (int i=0; i<N; ++i) {
            if ((100-progresses[i]) % speeds[i] == 0) {
                li.Add((100-progresses[i])/speeds[i]);
            }
            else {
                li.Add(((100-progresses[i])/speeds[i])+1);
            }
        }
        bool[] done = new bool[N];
        var ans = new List<int>();
        for (int i=0; i<N; ++i) {
            if (done[i]) {
                continue;
            }
            int cnt=0;
            for (int j=i; j<N; ++j) {
                if ((li[j] <= li[i]) && !done[j]) {
                    cnt++;
                    done[j] = true;
                }
                else {
                    break;
                }
            }
            ans.Add(cnt);
        } 
        return ans.ToArray();      
                
    }
}