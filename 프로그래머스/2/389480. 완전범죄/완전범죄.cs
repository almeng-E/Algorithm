using System;

public class Solution {
    public int solution(int[,] info, int n, int m) {
        // DP[x]: A의 누적이 x일때 가능한 누적 b의 최솟값
        int[] DP = new int[n];
        int INF = m;
        Array.Fill(DP, INF);
        DP[0] = 0;
        
        for (int i=0; i<info.GetLength(0); ++i) {
            int curA = info[i,0];
            int curB = info[i,1];
            
            for (int x=n-1; x>=0; --x) {
                int takeA = INF;
                if (x-curA >=0) {
                    takeA = DP[x-curA];
                }
            
                int takeB = DP[x]+curB;
                
                DP[x] = Math.Min(takeA, takeB);
            }
        }
        
        for (int x=0; x<n; ++x) {
            if (DP[x]<m) {
                return x;                
            }
        }
        
        
        return -1;
    }
}