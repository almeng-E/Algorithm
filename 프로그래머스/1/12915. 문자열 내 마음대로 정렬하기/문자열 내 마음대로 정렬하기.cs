using System;

public class Solution {
    public string[] solution(string[] strings, int n) {
        Array.Sort(strings, (a, b) => {
            // 1순위
            int sn = a[n].CompareTo(b[n]);
            if (sn!=0) return sn;
            
            // 2순위
            return a.CompareTo(b);
        });
        
        
        
        return strings;
    }
}