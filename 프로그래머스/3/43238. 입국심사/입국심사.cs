using System;

public class Solution {
    long ANS;
    int[] TIME;
    int N;
    
    public bool check(long mid) {
        long cnt = 0;
        for (int i=0; i<TIME.Length; ++i) {
            cnt += mid/TIME[i];
        }
        if (cnt>=N) return true;
        return false;
    }
    
    
    public long solution(int n, int[] times) {
        ANS = 0;
        TIME = times;
        N = n;
        
        long l = 0;
        long r = 1_000_000_000_000_000_000L;
        while (l <= r) {
            long mid = (l+r) >> 1;
            if (check(mid)) {
                // 가능
                ANS = mid;
                r = mid-1;
            }    
            else {
                // 불가능
                l = mid+1;
            }
        }
        
        return ANS;
    }
}