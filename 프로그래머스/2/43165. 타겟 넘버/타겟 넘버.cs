using System;

public class Solution {
    int CNT;
    int N;
    int TG;
    int[] NUMS;
    public int solution(int[] numbers, int target) {
        CNT = 0;
        N = numbers.Length;
        TG = target;
        NUMS = numbers;
        DFS(0, 0);
        
        return CNT;
    }
    
    public void DFS(int idx, int cur) {
        if (idx == N) {
            if (cur == TG) {
                CNT++;
            }
            return;
        }
        DFS(idx+1, cur+NUMS[idx]);
        DFS(idx+1, cur-NUMS[idx]);
    }   
    
    
}