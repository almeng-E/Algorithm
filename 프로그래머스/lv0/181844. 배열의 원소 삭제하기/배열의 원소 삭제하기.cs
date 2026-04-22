using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        HashSet<int> delSet = new HashSet<int>(delete_list);
        
        List<int> list = new List<int>();
        foreach (int a in arr){
            if (!delSet.Contains(a)){
                 list.Add(a);
            }
        }
        int[] answer = list.ToArray();
        
        return answer;
    }
}