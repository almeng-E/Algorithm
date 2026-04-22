using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        if ((a%2 == 1) && (b%2 == 1)) {
            answer += a*a;
            answer += b*b;
        } else if ((a%2 == 0) && (b%2 == 0)) {
            answer += Math.Abs(a-b);
        } else {
            answer += 2*(a+b);
        }
                
        return answer;
    }
}