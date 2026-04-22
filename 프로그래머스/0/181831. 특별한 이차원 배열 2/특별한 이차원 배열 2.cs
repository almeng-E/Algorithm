using System;

public class Solution {
    public int solution(int[,] arr) {
        int N = arr.GetLength(0);
        for (int i=0; i<N; ++i){
            for (int j=i; j<N; ++j) {
                if (arr[i,j] != arr[j,i]) {
                    return 0;
                }
            }
        }
        
        
        return 1;
    }
}