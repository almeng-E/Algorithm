using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[,] solution(int[,] arr) {
        int N = arr.GetLength(0);
        int M = arr.GetLength(1);
        int size = Math.Max(N, M);
        int[,] answer = new int[size,size];
        for (int i=0; i<N; ++i) {
            for (int j=0; j<M; ++j) {
                answer[i, j] = arr[i, j];
            }
        }
        
        
        
        return answer;
    }
}