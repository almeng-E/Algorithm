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
            
            var tmp = array.Skip(i).Take(j-i+1).ToList();
            tmp.Sort();
            answer[qi] = tmp[k];
        }
        return answer;
    }
}