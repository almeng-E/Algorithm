using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int passed = 0;
        var bridge = new Queue<int>(Enumerable.Repeat(0, bridge_length));
        int cur_b_w = 0;
        var truck = new Queue<int>(truck_weights);
        int t = truck_weights.Length;
        while (passed < t) {
            answer++;
            int old = bridge.Dequeue();
            if (old != 0) {
                passed++;
                cur_b_w -= old;
            };
            int nxt = 0;
            if (truck.Count > 0) {
                nxt = truck.Peek();
                if ((nxt+cur_b_w) <= weight) {
                    truck.Dequeue();
                } 
                else {
                    nxt = 0;
                }
            }
            cur_b_w += nxt;
            bridge.Enqueue(nxt);
            
        }
        
        
        
        return answer;
    }
}