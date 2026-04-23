using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] answers) {
        var ret = new List<int>();        
        int[] a1 = new int[]{1, 2, 3, 4, 5};
        int[] a2 = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] a3 = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        var scores = new List<int>();
        scores.Add(0);
        scores.Add(calc(a1, answers));
        scores.Add(calc(a2, answers));
        scores.Add(calc(a3, answers));
        
        int maxScore = 0;
        for (int i=1; i<4; ++i) {
            if (maxScore < scores[i]) {
                maxScore = scores[i];
                ret.Clear();
                ret.Add(i);
            }
            else if (maxScore == scores[i]) {
                ret.Add(i);
            }
        }
        
        
        var answer = ret.ToArray();
        return answer;
    }

    public int calc(int[] person, int[] answers) {
        int N = answers.Length;
        int M = person.Length;
        int ret = 0;
        for (int i=0; i<N; ++i) {
            if (answers[i] == person[i%M]) ret += 1;
        }
        return ret;
    }


}