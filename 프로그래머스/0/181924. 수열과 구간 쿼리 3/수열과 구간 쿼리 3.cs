using System;

public class Solution {
    public int[] solution(int[] arr, int[,] queries) {
        int N = queries.GetLength(0);
        for (int i=0; i<N; ++i) {
            int l = queries[i, 0];
            int r = queries[i, 1];
            int tmp = 0;
            tmp = arr[l];
            arr[l] = arr[r];
            arr[r] = tmp;
        }
        
        return arr;
    }
}