using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] arr) {
        List<int> ans = new List<int>();
        foreach (int e in arr){
            for (int i=0; i<e; ++i){
                ans.Add(e);
            }
        }
        return ans.ToArray();
        
    }
}