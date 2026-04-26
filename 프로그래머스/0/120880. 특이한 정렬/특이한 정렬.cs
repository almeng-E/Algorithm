using System;

public class Solution {
    public int[] solution(int[] numlist, int n) {
        Array.Sort(numlist, (a, b) => {
            // 1순위
            int dComp = Math.Abs(a-n).CompareTo(Math.Abs(b-n));
            if (dComp!=0) return dComp;
            
            // 2순위
            return b.CompareTo(a);
        });
        
        return numlist;
    }
}