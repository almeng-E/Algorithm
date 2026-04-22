using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] num_list) {
        Array.Sort(num_list);
        int N = num_list.Length-5;
        int[] answer = new int[N];
        for (int i=0; i<N; ++i){
            answer[i] = num_list[i+5];
        }
        
        return answer;
    }
}