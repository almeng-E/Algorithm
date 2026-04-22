using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        foreach (int e in num_list){
            if (e == n){
                answer = 1;
            }
        }
        
        return answer;
    }
}