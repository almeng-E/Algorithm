using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string[,] clothes) {
        var dict = new Dictionary<string, int>();
        int N = clothes.GetLength(0);
        for (int i=0; i<N; ++i) {
            string t = clothes[i, 1];
            if (!dict.ContainsKey(t)) {
                dict[t] = 0;
            }
            dict[t] ++;
        }
        int answer = 1;
        foreach (int v in dict.Values) {
            answer *= (v+1);
        }
        answer -= 1;
        
        return answer;
    }
}