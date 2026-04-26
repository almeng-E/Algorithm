using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(string s) {
        int N = s.Length;
        var li = new List<int>();
        for (int i=0; i<N; ++i) {
            if ('0' <= s[i] && s[i] <= '9') {
                li.Add(s[i]-'0');
            }
        }
        li.Sort();
        
        int[] answer = li.ToArray();
        return answer;
    }
}