using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int n, int[,] computers) {
        int answer = 0;
        bool[] v = new bool[n];
        for (int i=0; i<n; ++i) {
            if (!v[i]) {
                answer++;
                v[i] = true;
                var q = new Queue<int>();
                q.Enqueue(i);
                while (q.Count>0) {
                    int cur = q.Dequeue();
                    for (int nxt=0; nxt<n; ++nxt) {
                        if (computers[cur,nxt] == 1 && !v[nxt]) {
                            v[nxt] = true;
                            q.Enqueue(nxt);
                        }
                    }
                    
                }
            }
        }
        
        
        
        return answer;
    }
}