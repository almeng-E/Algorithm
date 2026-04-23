using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        
        int cLen = commands.GetLength(0);
        int[] answer = new int[cLen];
        for (int qi=0; qi<cLen; ++qi) {
            int i = commands[qi,0] - 1;
            int j = commands[qi,1] - 1;
            int k = commands[qi,2] - 1;
            
            // 슬라이싱 어케하더라; arr랑 list 헷갈림;
            var tmp = new List<int>();
            for (int idx=i; idx<=j; ++idx) {
                tmp.Add(array[idx]);
            }
            tmp.Sort();
            answer[qi] = tmp[k];
        }
        return answer;
    }
}