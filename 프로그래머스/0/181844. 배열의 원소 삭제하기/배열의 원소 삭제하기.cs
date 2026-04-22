using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<int> list = new List<int>();
        
        foreach (int a in arr) {
            bool isFound = false;
            foreach (int d in delete_list){
                if (a == d){
                    isFound = true;
                }
            }
            if (!isFound){
                list.Add(a);
            }
        }
                
        int[] answer = list.ToArray();
        
        return answer;
    }
}