using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        int[] answer = new int[commands.GetLength(0)];
        for (int ci=0; ci<commands.GetLength(0); ++ci) {
            int i=commands[ci,0] -1 , j=commands[ci,1] -1, k=commands[ci,2] -1;
            var li = new List<int>();
            for (int x=i; x<=j; ++x) {
                li.Add(array[x]);
            }
            li.Sort();
            answer[ci] = li[k];            
        }
        
        return answer;
    }
}