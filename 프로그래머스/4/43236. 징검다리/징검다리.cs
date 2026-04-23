using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    int N;
    List<int> DIST;
        
    public bool check(int mid) {
        int removeCnt = 0;
        int curD = 0;
        for (int i=0; i<DIST.Count; ++i){
            curD += DIST[i];
            
            if (curD < mid) {
                removeCnt++;
            }
            else {
                curD = 0;
            }
        }
        
        if (removeCnt <= N) return true;
        return false;
    }
    
    public int solution(int distance, int[] rocks, int n) {
        N = n;
        DIST = new List<int>();
        
        var rock = rocks.ToList();
        rock.Add(0);
        rock.Add(distance);
        rock.Sort();
        for (int i=1; i<rock.Count; ++i) {
            DIST.Add(rock[i]-rock[i-1]);
        }
        
        int answer = 0;
        
        int l = 0;
        int r = distance;
        while (l <= r) {
            int mid = (l+r)>>1;
            if (check(mid)) {
                // 가능
                answer = mid;
                l = mid+1;
            }
            else {
                // 불가능
                r = mid-1;
            }
        }
        
        
        
        return answer;
    }
}